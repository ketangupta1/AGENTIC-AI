## 🚀 Graph Memory and knowldege Graph in AI Agents

### Why graph is needed
- When we adding chats into the memory it doesnt stores the relationship.
- e.g: John and Elen is the employee of company X, then whats the relationship between John and Elen can't predicted by the vector DB.
- So, to overcome this Graph memory comes into the picture, bcz it stores the relationship as well along with the data.

---

### Setting Up neo4j graph cloud instance for graph Memory
- As neo4j is very heavy so we will setup cloud instance.
- Setup neo4j account and create the instance.
- We can query these database with the help of Cypher query.

---

### Adding Graph database support for memory
- Copy the connection uri from neo4j cloud.
- pip install langchain-neo4j
- pip install rank-bm25
- Add your graph_store creds in the config so that the info can be stored in the graph.
- And knowledge graph for the user will be created.
- Run the application mem0_using_graph_neo4j and create your knowledge graph.