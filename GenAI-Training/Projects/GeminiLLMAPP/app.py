# app.py — Streamlit Q&A with model listing + robust error handling
from dotenv import load_dotenv
import os
import textwrap
import streamlit as st
import google.generativeai as genai
from requests import HTTPError

# ---- Load env and configure client ----
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found in .env (create .env with GOOGLE_API_KEY=...)")
genai.configure(api_key=API_KEY)

# ---- Helpers ----
def safe_list_models():
    """
    Try to list models via the client API. If the client's list_models() is unavailable
    or buggy, return None and let the UI fallback to a safe small list.
    """
    try:
        # Many client versions have genai.list_models()
        models_iter = genai.list_models()
        # Convert to list of model ids/names (adapt to actual returned shape)
        models = []
        for m in models_iter:
            # m may be a dict-like; try common keys
            if isinstance(m, dict):
                models.append(m.get("name") or m.get("id") or str(m))
            else:
                # object with attributes
                for attr in ("name", "id", "model", "model_id"):
                    if hasattr(m, attr):
                        val = getattr(m, attr)
                        if val:
                            models.append(val)
                            break
                else:
                    models.append(str(m))
        return list(dict.fromkeys(models))  # dedupe & preserve order
    except Exception as e:
        # Return None to signal we couldn't list models programmatically
        return None

def extract_text_from_response(resp):
    """Extract text from response returned by model.generate_content(...)"""
    try:
        if hasattr(resp, "text") and resp.text:
            return resp.text
        for attr in ("output", "content"):
            if hasattr(resp, attr) and getattr(resp, attr):
                return getattr(resp, attr)
        if hasattr(resp, "candidates") and resp.candidates:
            cand = resp.candidates[0]
            for attr in ("content", "output", "text"):
                if hasattr(cand, attr) and getattr(cand, attr):
                    return getattr(cand, attr)
    except Exception:
        pass
    try:
        return str(resp)
    except Exception:
        return "<unreadable response>"

def get_gemini_response(prompt: str, model_name: str):
    if not prompt or not prompt.strip():
        return "Please enter a question."

    try:
        model = genai.GenerativeModel(model_name)
        resp = model.generate_content(prompt)
        return extract_text_from_response(resp)
    except Exception as e:
        # If the API responded with a 404 about the model, surface a helpful message
        msg = str(e)
        if "404" in msg and "not found" in msg.lower():
            return ("Model not found (404). The selected model is not available for your API/version. "
                    "Please choose a different model from the dropdown or run 'Refresh model list'.")
        return f"Error calling Gemini API: {e}"

# ---- Streamlit UI ----
st.set_page_config(page_title="Gemini Q&A (model-safe)", layout="centered")
st.title("💬 Gemini Q&A — safe model selection")

st.markdown("This app will try to list available models from the API. If that fails, pick a model from a fallback list.")

# Try to fetch model list
models = safe_list_models()

if models:
    st.success(f"Found {len(models)} model(s) via API.")
    model_option = st.selectbox("Select model", options=models, index=0)
else:
    st.warning("Could not list models programmatically (client may be old or list_models is unavailable).")
    # Fallback options — adjust/remove depending on what your account supports
    fallback = [
        "gemini-1.5",
        "gemini-1.5-flash",
        "gemini-2.5-flash",
        "gemini-text-bison-001",  # Vertex-style name (if you use Vertex)
    ]
    model_option = st.selectbox("Select model (fallback)", options=fallback, index=0)
    if st.button("Refresh model list"):
        st.experimental_rerun()

prompt = st.text_area("Enter your question here", height=140)

if st.button("Ask"):
    with st.spinner("Generating..."):
        answer = get_gemini_response(prompt, model_option)
    st.subheader("Response")
    st.markdown(textwrap.dedent(answer))

    # Optional dev info: show raw response (helpful during debugging)
    with st.expander("Raw API debug (dev only)"):
        try:
            model = genai.GenerativeModel(model_option)
            raw = model.generate_content(prompt)
            st.write(raw)
            st.write("Type:", type(raw))
            st.write("Attributes:", [a for a in dir(raw) if not a.startswith("_")])
        except Exception as ex:
            st.write("Could not fetch raw response for debug:", ex)
