cat > README.md << 'EOF'
# ShopAPI — DevOps Learning Project

A production-grade multi-service application used as a learning vehicle
for DevOps tools and practices.

## Services

| Service | Port | Description |
|---|---|---|
| Product Service | 8000 | CRUD for products, stores images in S3 |
| Order Service | 8001 | Creates orders, calls Product Service |
| PostgreSQL | 5432 | Shared database |

## Tech Stack

- **Orchestration:** Kubernetes (OrbStack)
- **GitOps:** ArgoCD
- **CI:** GitHub Actions
- **Registry:** GHCR
- **IaC:** Terraform
- **AWS Simulation:** MiniStack
- **Observability:** Prometheus + Grafana + Loki
- **Ingress:** Nginx Ingress Controller

## Project Structure

See learning plan for full directory structure and phase breakdown.

## Running Locally (Docker Compose)
docker compose up

## Deploying to Kubernetes
kubectl apply -k k8s/overlays/dev
EOF
