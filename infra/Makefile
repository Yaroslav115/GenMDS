PROJECT ?= genmds
COMPOSE ?= docker compose -f docker-compose.dev.yml

.PHONY: help
help:
\t@echo "Targets:"
\t@echo "  build         - собрать образы (api/worker/web)"
\t@echo "  up            - запустить все сервисы"
\t@echo "  down          - остановить и удалить контейнеры"
\t@echo "  restart       - перезапустить сервисы"
\t@echo "  test          - прогнать быстрые тесты"
\t@echo "  logs          - показать логи всех сервисов"
\t@echo "  logs-api      - показать логи API"
\t@echo "  logs-worker   - показать логи worker"
\t@echo "  logs-web      - показать логи web"
\t@echo "  logs-api-f    - фолловить логи API (живые)"
\t@echo "  logs-worker-f - фолловить логи worker (живые)"
\t@echo "  logs-web-f    - фолловить логи web (живые)"
\t@echo "  clean         - удалить dangling images/cache (осторожно)"
\t@echo "  prune-logs    - архивировать/урезать старые логи (роль rotate)"

build:
\tcd .. && $(COMPOSE) build --pull

up:
\tcd .. && $(COMPOSE) up -d

down:
\tcd .. && $(COMPOSE) down

restart: down up

test:
\t# API юнит-тесты
\tcd .. && $(COMPOSE) run --rm api sh -c \"pip install -q -r requirements.txt >/dev/null 2>&1 || true; pytest -q\"
\t# *Опционально:* фронтенд юнит-тесты
\t# cd .. && $(COMPOSE) run --rm web sh -c \"npm ci && npm test -- --watch=false\"

logs:
\tcd .. && $(COMPOSE) logs --tail=200

logs-api:
\tcd .. && $(COMPOSE) logs --tail=200 api
logs-worker:
\tcd .. && $(COMPOSE) logs --tail=200 worker
logs-web:
\tcd .. && $(COMPOSE) logs --tail=200 web

logs-api-f:
\tcd .. && $(COMPOSE) logs -f api
logs-worker-f:
\tcd .. && $(COMPOSE) logs -f worker
logs-web-f:
\tcd .. && $(COMPOSE) logs -f web

clean:
\tdocker image prune -f
\tdocker builder prune -f

prune-logs:
\tfind ../logs -type f -name \"*.log\" -size +50M -exec gzip -f {} \\; || true

