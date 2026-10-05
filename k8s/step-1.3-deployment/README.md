# Step 1.3 - Deployment

Step 1.2 created a raw Pod. This step replaces that approach with a Kubernetes Deployment.

## Architecture

```text
Deployment             <- Desired state
     |
     v
ReplicaSet             <- Replica management
     |
     +------> Pod 1     <- Run container
     |
     +------> Pod 2     <- Run container
```

## Why Deployment?

A Deployment tells Kubernetes the desired state of the application, including how many replicas should exist and which Pod template to use.

If a managed Pod disappears, the Deployment works through its ReplicaSet to create a replacement.

### Why 2 replicas?

```text
replicas: 2
← Learn redundancy
```

Two replicas let us demonstrate that the application is not tied to one Pod. Later, a Service will distribute traffic across them.

### Why not manage Pods directly?

A raw Pod is useful for learning, debugging, and one-off workloads, but it is the wrong abstraction for a continuously running application.

### Why not 10 replicas?

Because this is a small learning workload. More replicas consume resources without teaching us anything additional at this stage.

## Resource requests and limits

```text
requests
← Scheduling requirement

limits
← Resource ceiling
```

We introduce them now because resource management becomes important when Kubernetes schedules workloads onto a constrained cluster.

## Apply

Build the image first:

```bash
docker build -t mcp-platform:0.1.0 ./app/mcp-server
```

If using kind:

```bash
kind load docker-image mcp-platform:0.1.0
```

Apply the Deployment:

```bash
kubectl apply -f k8s/step-1.3-deployment/deployment.yaml
```

Check:

```bash
kubectl get deployment
kubectl get replicasets
kubectl get pods -o wide
```

## Experiment: delete a Pod

Find a Pod:

```bash
kubectl get pods
```

Delete it:

```bash
kubectl delete pod <pod-name>
```

Then immediately run:

```bash
kubectl get pods -w
```

You should see Kubernetes create a replacement.

## What to learn

- Deployment
- ReplicaSet
- Desired state
- Replica management
- Pod replacement
- Resource requests
- Resource limits

## Next

Step 1.4 introduces a Service.

```text
Deployment
     |
     v
Pods
  /   \
Pod 1  Pod 2
  \   /
   v v
 Service              <- Stable endpoint
```

The Service solves a problem that the Deployment does not: **stable network access to changing Pods**.
