import express from "express";
import morgan from "morgan";
import swaggerUi from "swagger-ui-express";
import specs from "./docs/swagger";

const app = express();
const PORT = 3000;

// Middleware para manejar datos JSON
app.use(express.json());

// Middleware para registrar solicitudes
app.use(morgan("dev"));

// Integrar Swagger
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(specs));

app.listen(PORT, () => {
  console.log(`Server listen: http://localhost:${PORT}`);
});
