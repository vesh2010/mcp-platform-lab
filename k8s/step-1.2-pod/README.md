# Step 1.2 - First Kubernetes Pod

This is the first Kubernetes workload in the project.

## Architecture

```text
Kubernetes
    |
    v
Pod                    <- Runs container
    |
    v
MCP container          <- Runs application
```

## Why a Pod?

A **Pod** is the smallest deployable unit in Kubernetes. It provides the execution environment for one or more containers that share networking and storage.

For this first exercise we intentionally use one container in one Pod.

### Why not Deployment yet?

A Deployment is better for a real application because it manages Pod lifecycle and replicas. We will introduce it in Step 1.3.

### Why not Service yet?

A Service provides stable network access to Pods. We don't need it yet because this step is specifically about understanding the Pod itself.

## Important limitation

A Pod is **not** normally something you manage directly for production workloads. Kubernetes can replace a Pod, but a standalone Pod does not provide the desired-state management that a Deployment provides.

## Local image

The manifest expects:

```text
mcp-platform:0.1.0
```

Build that image locally before creating the Pod.

For kind:

```bash
kind load docker-image mcp-platform:0.1.0
```

Then:

```bash
kubectl apply -f k8s/step-1.2-pod/pod.yaml
kubectl get pod mcp-server
kubectl describe pod mcp-server
```

Check the application:

```bash
kubectl port-forward pod/mcp-server 8080:8080
```

Then open:

```text
http://localhost:8080/health
```

## What to observe

```bash
kubectl get pod -o wide
kubectl logs mcp-server
kubectl exec -it mcp-server -- sh
```

The goal is to understand:

- Pod lifecycle
- Container inside a Pod
- Pod IP
- Container port
- Logs
- Basic `kubectl` interaction
- Why directly managing Pods is limited

## Next

Step 1.3 introduces a **Deployment**.

```text
Deployment       <- Desired state
      |
      v
ReplicaSet        <- Replica management
      |
      v
Pod               <- Runs container
```
