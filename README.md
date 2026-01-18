# ☁️ Da monolite locale a AWS ECS: Cloud Migration

Questo progetto dimostra la migrazione di un'applicazione multi-tier da un ambiente DOcker Compose locale a un'architettura production-ready su **AWS ECS Fargate**, gestita via **Terraform**.

## Architettura

L'app segue una classica architettura a 3-tier, con aggiunta di un "Seeder" per l'inizializzazione del DB.
Prima di lanciare il task di seeding noterete infatti che il frontend rimane in attesa che il DB venga popolato.

  <img width="991" height="627" alt="ethan-demo-locale" src="https://github.com/user-attachments/assets/29f4ebfa-c7b7-4fad-afb2-96c16f56ad16" />

