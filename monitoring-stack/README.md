# Containerised Monitoring Stack (Prometheus + Grafana)

A one-command monitoring lab with Docker Compose: a Flask app instrumented with Prometheus metrics, host metrics, dashboards and alert rules.

## Architecture

```
loadgen ──► app :5000/metrics ─┐
                               ├──► Prometheus :9090 ──► Grafana :3000
node-exporter :9100 ───────────┘          │
                                          └──► Alertmanager :9093
```

| Service | Role |
|---------|------|
| `app` | Flask demo app exposing `/metrics` (request count, latency histogram). `/flaky` returns random 500s |
| `loadgen` | Sends continuous traffic so dashboards have live data |
| `node-exporter` | Host CPU / memory / disk metrics |
| `prometheus` | Scrapes every 5s, evaluates alert rules |
| `alertmanager` | Groups and routes alerts (webhook placeholder, easily swapped for email/Slack) |
| `grafana` | Auto-provisioned datasource and dashboard |

## Run

```bash
docker compose up -d --build
```

- Grafana: http://localhost:3000 (admin / admin), dashboard **App & Host Overview**
- Prometheus: http://localhost:9090 (see the **Alerts** tab)
- Alertmanager: http://localhost:9093

## Alerts (`prometheus/alerts.yml`)

`InstanceDown`, `HighErrorRate` (>5% 5xx), `HighLatencyP95` (>300ms), `HighCPU` (>85%).
Try it: `docker compose stop app` and watch `InstanceDown` fire after 30s.

## Nagios / Splunk comparison

| Concept | Nagios | Splunk | This stack |
|---------|--------|--------|-----------|
| Collection | Active checks / NRPE | Forwarders, log ingestion | Pull-based metric scraping |
| Alerting | Host/service check thresholds | Saved-search alerts | PromQL rules + Alertmanager |
| Dashboards | Limited | Strong for logs | Grafana for time-series metrics |

Prometheus focuses on numeric metrics; for logs you would add Loki, which plugs into the same Grafana.

## Tear down
```bash
docker compose down -v
```
