# MCP Platform Lab

A hands-on Kubernetes and platform-engineering lab for building and operating an MCP service on Oracle Cloud Infrastructure (OCI).

## Project goal

Build a small, production-style MCP platform while learning Kubernetes one layer at a time.

The project will progress from local Kubernetes to Oracle Kubernetes Engine (OKE), then add database persistence, Gateway API routing, canary releases, Terraform, CI/CD, GitOps, and observability.

## Architecture evolution

### Phase 0: Local Kubernetes

```text
Laptop
  |
  v
Service              <- Stable endpoint
  |
  v
Deployment           <- Manage replicas
  |
  v
Pod                  <- Run application
```

**Why:** Learn Kubernetes without cloud complexity.

**Alternative:** Docker Compose  
**Why not:** Does not teach Kubernetes scheduling, services, probes, or controllers.

### Phase 1: OCI / OKE

```text
Internet
   |
   v
OCI Load Balancer    <- External entry
   |
   v
OKE Service          <- Stable endpoint
   |
   v
MCP Pods             <- Run application
```

**Why:** Learn the cloud-to-Kubernetes boundary.

**Alternative:** NodePort  
**Why not:** Simpler, but less production-like for this project.

### Phase 2: Persistence

```text
MCP Pods
   |
   v
Oracle Autonomous DB <- Persistent data
```

**Why:** Kubernetes should run the application; the managed database provides durable state.

**Alternative:** Oracle DB inside Kubernetes  
**Why not:** Adds database-operations complexity that is outside the initial learning goal.

### Phase 3: Routing

```text
OCI Load Balancer    <- External entry
   |
   v
Gateway API          <- Smart routing
   |
   v
HTTPRoute            <- Traffic rules
   |
   +-------> MCP v1  <- Stable version
   |
   +-------> MCP v2  <- New version
```

**Why:** Learn modern Kubernetes traffic management.

**Alternative:** Ingress  
**Why not:** Useful and simpler, but Gateway API is a better fit for header routing and traffic splitting.

### Phase 4: Canary

```text
Gateway
  |
  +---- 90% ----> MCP v1   <- Stable
  |
  +---- 10% ----> MCP v2   <- Canary
```

**Why:** Release new versions gradually.

### Phase 5: Platform controls

```text
Namespace             <- Environment isolation
ResourceQuota         <- Resource budget
NetworkPolicy         <- Traffic isolation
Affinity              <- Placement control
Probes                <- Health detection
```

**Why:** Learn the operational controls behind production workloads.

### Phase 6: Infrastructure as Code

```text
Terraform
   |
   +----> VCN            <- Network
   +----> OKE            <- Compute
   +----> OCI resources  <- Cloud infrastructure
```

**Why:** Rebuild infrastructure consistently.

**Alternative:** OCI CLI / Console  
**Why not:** Good for one-off operations, weaker as the source of truth for infrastructure.

### Phase 7: CI/CD

```text
Git push
   |
   v
GitHub Actions       <- Automated delivery
   |
   v
Container Registry   <- Store images
   |
   v
OKE                  <- Run release
```

**Why:** Remove manual build and deployment steps.

### Phase 8: GitOps

```text
Git
 |
 v
Argo CD              <- Desired-state sync
 |
 v
OKE
```

**Why:** Make Git the deployment source of truth.

### Phase 9: Observability

```text
MCP
 |
 +----> Metrics       <- Measure health
 +----> Logs          <- Debug failures
 +----> Traces        <- Follow requests
```

**Why:** Canary and production decisions need evidence.

## Final target

```text
                              Internet
                                  |
                                  v
                       OCI Load Balancer
                         <- External entry
                                  |
                                  v
                           Gateway API
                         <- Smart routing
                                  |
                                  v
                            HTTPRoute
                         <- Traffic rules
                           /          \
                          /            \
                    Stable 90%      Canary 10%
                       |                |
                       v                v
                    MCP v1           MCP v2
                    <- Stable        <- New version
                       \                /
                        \              /
                         v            v
                            Service
                       <- Stable discovery
                                  |
                                  v
                     Oracle Autonomous DB
                        <- Persistent state


GitHub
   |
   v
GitHub Actions             <- Automated CI/CD
   |
   v
Container Registry         <- Image storage
   |
   v
Argo CD                    <- GitOps sync
   |
   v
OKE


Terraform                  <- Infrastructure code
   |
   +---- VCN               <- Network
   +---- OKE               <- Compute
   +---- OCI resources     <- Cloud infrastructure
```

## Learning roadmap

- [ ] Phase 0: Local Kubernetes fundamentals
- [ ] Phase 1: OKE cluster
- [ ] Phase 2: MCP application
- [ ] Phase 3: Oracle Autonomous Database
- [ ] Phase 4: Gateway API
- [ ] Phase 5: Header routing
- [ ] Phase 6: Canary releases
- [ ] Phase 7: Scheduling and resource controls
- [ ] Phase 8: NetworkPolicy and RBAC
- [ ] Phase 9: Terraform
- [ ] Phase 10: GitHub Actions
- [ ] Phase 11: GitOps with Argo CD
- [ ] Phase 12: Observability
- [ ] Phase 13: Platform automation

## Repository structure

Planned structure:

```text
mcp-platform-lab/
├── app/
├── k8s/
├── terraform/
├── .github/
├── scripts/
└── README.md
```

We will add each directory only when its phase starts. This keeps the repository understandable and makes the learning progression visible.

## Cost target

The lab is designed to stay within OCI Always Free resources where practical. Resource usage will be kept intentionally small, and expensive components will not be added unless they solve a specific learning problem.

## Status

**Current phase:** Phase 0 planning

**Next build:** Local MCP application + Deployment + Service + ConfigMap + Secret + liveness/readiness probes
