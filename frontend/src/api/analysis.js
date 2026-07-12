import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export async function analyzeRepository(repoUrl) {
  const response = await api.post("/analyze", {
    repo_url: repoUrl,
  });

  return response.data;
}