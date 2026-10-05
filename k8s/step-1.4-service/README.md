# Step 1.4 — Service

## Goal

Give the MCP server a **stable network endpoint**.

Pods are disposable. Their IP addresses can change whenever a Pod is recreated. A Kubernetes Service provides a stable virtual IP and DNS name and sends traffic to matching Pods.

## Architecture

```
Client
  |
Service                  ← Stable endpoint
  |
  +---- Pod A            ← Run application
  |
  +---- Pod B            ← Run application
```

The Service selects Pods using:

```yaml
selector:
  app: mcp-server
```

Both Deployment Pods have this label, so the Service can route traffic to them.

## Why ClusterIP?

```
ClusterIP
← Internal access
```

It is the default Service type and is appropriate here because we only need stable communication inside the cluster.

### Alternatives

```
NodePort
← Simple external access
Why not now: Less realistic for our target architecture

LoadBalancer
← Cloud external access
Why not now: OCI Load Balancer comes later with Gateway API
```

We will eventually expose the application through:

```
Internet
   |
OCI Load Balancer        ← External entry
   |
Gateway API              ← Smart routing
   |
Service                  ← Stable endpoint
   |
Pods                     ← Run application
```

## Hands-on

Build/load the image if needed:

```bash
docker build -t mcp-platform:0.1.0 ./app/mcp-server
kind load docker-image mcp-platform:0.1.0
```

Apply the Deployment and Service:

```bash
kubectl apply -f k8s/step-1.3-deployment/deployment.yaml
kubectl apply -f k8s/step-1.4-service/service.yaml
```

Inspect:

```bash
kubectl get pods -o wide
kubectl get deployment
kubectl get service
kubectl describe service mcp-server
```

You should see a ClusterIP assigned to `mcp-server`.

Check the Service endpoints:

```bash
kubectl get endpoints mcp-server
```

The endpoints should contain the IPs of the two MCP Pods.

## Test the Service

Port-forward the Service:

```bash
kubectl port-forward service/mcp-server 8080:8080
```

Then open:

```
http://localhost:8080/health
http://localhost:8080/info
```

The important difference is that you are now connecting to the **Service**, not directly to a Pod.

## Prove Service discovery

Run:

```bash
kubectl run curl --image=curlimages/curl:8.10.1 -it --rm --restart=Never -- \
  curl http://mcp-server:8080/info
```

The hostname `mcp-server` resolves through Kubernetes DNS.

## Prove Pod replacement

Delete one Pod:

```bash
kubectl delete pod <pod-name>
```

Then:

```bash
kubectl get pods -w
```

The Deployment creates a replacement Pod.

The Service continues using the stable Service endpoint.

## What you learned

- Pod IP = disposable
- Service IP = stable
- Service selector = finds Pods
- ClusterIP = internal access
- Kubernetes DNS = service discovery
- Deployment + Service = basic application networking

## Next

**Step 1.5 — ConfigMap**

We will move non-secret configuration such as `APP_VERSION` and `ENVIRONMENT` out of the container definition.

Architecture:

```
ConfigMap                ← Non-secret config
      |
Deployment               ← Inject config
      |
Pods                     ← Run with config
```
