## Final System Architecture
                    ┌──────────────┐
                    │    GitHub    │
                    └──────┬───────┘
                           │
                    GitHub Actions
                           │
          ┌────────────────┴──────────────┐
          │                               │
     Docker Build                   Terraform
          │                               │
   Container Registry             AWS Infrastructure
          │                               │
          └──────────────┬────────────────┘
                         │
                    Kubernetes
                         │
              ConfigMaps / Secrets
                         │
                    Application
                         │
                     Database