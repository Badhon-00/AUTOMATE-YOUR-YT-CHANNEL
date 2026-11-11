import "dotenv/config";
import express from "express";
import { z } from "zod";

const app = express();
app.disable("x-powered-by");
app.use(express.json({ limit: "1mb" }));

const port = Number(process.env.PORT ?? 4000);
const requestSchema = z.object({ name: z.string().trim().min(1).max(80) });

app.get("/health", (_req, res) => {
  res.status(200).json({
    status: "ok",
    service: "youtube-music-manager-api",
    timestamp: new Date().toISOString()
  });
});

app.post("/api/v1/projects/validate", (req, res) => {
  const parsed = requestSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: "Invalid request", details: parsed.error.flatten() });
  }
  return res.status(200).json({ valid: true, project: parsed.data });
});

app.listen(port, () => {
  console.log(`API listening on :${port}`);
});
