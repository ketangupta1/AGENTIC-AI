## 🚀 Convertational Agentic AI with Voice Agents and Chained Patterns

### Understanding Convertational AI for Agents
- Till now we were typing and giving it to LLM and LLM was giving response.
- Here we will speak and fed it to LLM and in return we will get the voice responses from agents.
- Two types of model architecture S2S and chained architecture.

---

### Speech to speech models
- Agent will take the user speech and process it and return speech in the response.
- It is realtime system no latency.
- It is scoped to one thing only, you can build a specific agent for customer support.
- It is very expensive.
- gpt-4o-realtime-preview model is eg of s2s.
- Technically how s2s works, internally its kind of chained model.

---

### Chained Model
- User_voice -> Text(STT) -> LLM -> Text -> Audio(TTS)
- The advantage of this architecture is you can use any LLM.
- Here we are not binded to specific model we can choose any LLM and any model of that LLM.
- Here we can do anything we can use tool, we can use langGraph, langchain.