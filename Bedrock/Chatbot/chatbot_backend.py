# chatbot_backend_fixed_system_retry.py
from typing import Any, List, Dict
from langchain_aws import ChatBedrockConverse

def get_llm(profile: str = "default", model_id: str = "amazon.titan-text-lite-v1", temperature: float = 0.1, max_tokens: int = 500):
    return ChatBedrockConverse(
        credentials_profile_name=profile,
        model=model_id,
        temperature=temperature,
        max_tokens=max_tokens,
    )

def extract_assistant_text(resp: Any) -> str:
    if resp is None:
        return ""
    if hasattr(resp, "content"):
        return resp.content
    if isinstance(resp, dict):
        for key in ("messages", "output"):
            try:
                return resp[key][0]["content"][0]["text"]
            except Exception:
                pass
        if "content" in resp:
            return resp["content"]
    if isinstance(resp, list) and len(resp) > 0 and isinstance(resp[0], dict):
        try:
            return resp[0]["content"][0]["text"]
        except Exception:
            pass
    return str(resp)

class SimpleHistory:
    def __init__(self, max_turns: int = 6):
        self.max_turns = max_turns
        self.messages: List[Dict[str, str]] = []
    def add_user(self, text: str):
        self.messages.append({"role": "user", "text": text}); self._trim()
    def add_assistant(self, text: str):
        self.messages.append({"role": "assistant", "text": text}); self._trim()
    def _trim(self):
        if len(self.messages) > self.max_turns * 2:
            self.messages = self.messages[-(self.max_turns * 2):]
    def to_bedrock_messages(self, system_prompt: str = None) -> List[Dict[str, object]]:
        out = []
        if system_prompt:
            out.append({"role": "system", "content": [{"text": system_prompt}]})
        for m in self.messages:
            out.append({"role": m["role"], "content": [{"text": m["text"]}]})
        return out

def demo_converse(user_text: str, llm: ChatBedrockConverse, history: SimpleHistory, system_prompt: str = None) -> str:
    history.add_user(user_text)
    messages = history.to_bedrock_messages(system_prompt=system_prompt)

    # Try to call once, if model rejects system messages, retry without system role.
    try:
        resp = llm.invoke(messages)
    except Exception as e:
        msg = str(e).lower()
        if "system messages" in msg or "doesn't support system messages" in msg or "does not support system messages" in msg:
            # Retry without system role
            messages_no_system = [m for m in messages if m.get("role") != "system"]
            try:
                resp = llm.invoke(messages_no_system)
            except Exception:
                # As a last-ditch effort, merge the system prompt into the user text and retry
                merged_user = (system_prompt + "\n\n" + user_text) if system_prompt else user_text
                merged_messages = []
                # use history but convert system->prepend to latest user message
                for m in history.messages[:-1]:  # all prior turns except latest user
                    merged_messages.append({"role": m["role"], "content": [{"text": m["text"]}]})
                merged_messages.append({"role": "user", "content": [{"text": merged_user}]})
                resp = llm.invoke(merged_messages)
        else:
            # unexpected error: re-raise so caller can see it
            raise

    assistant_text = extract_assistant_text(resp)
    history.add_assistant(assistant_text)
    return assistant_text

# --------- quick demo ----------
if __name__ == "__main__":
    PROFILE = "default"
    MODEL_ID = "amazon.titan-text-lite-v1"  # change to a model you have access to
    llm = get_llm(profile=PROFILE, model_id=MODEL_ID)

    history = SimpleHistory(max_turns=6)
    # Try using a system prompt — script will auto-retry if the model rejects it.
    system_prompt = "You are a helpful assistant; keep answers short."

    questions = [
        "What is Amazon Bedrock?",
        "How would I integrate it into my web app?",
    ]

    for q in questions:
        print("USER:", q)
        reply = demo_converse(q, llm, history, system_prompt=system_prompt)
        print("ASSISTANT:", reply)
        print("-" * 60)
