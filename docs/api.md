# API para reservar sala de reunião

## End Points Para Gestão das Salas

* `GET    /api/meeting-room/` - Lista as salas criadas no sistema
* `GET    /api/meeting-room/?search=termo` - Listar as salas criadas, filtrando pelo "termo"
* `POST   /api/meeting-room/` - Registrar uma nova sala de reunião
* `PATCH  /api/meeting-room/:id/` - Editar uma sala de reunião existente
* `DELETE /api/meeting-room/:id/` - Remover uma sala de reunião existente

### Exemplos de requisição de criação de sala

```json
{
"name": "Sala Principal",
"place": "5 andar",
"description": "Curabitur pellentesque faucibus arcu a varius."
}
```

## End Points Para Gestão de Reservas

* `GET    /api/meeting/` - Lista as reservas criadas no sistema
* `GET    /api/meeting/?search=termo` - Listar as reservas criadas, filtrando pelo "termo"
* `POST   /api/meeting/` - Registrar uma nova reserva
* `PATCH  /api/meeting/:id/` - Editar uma reserva existente
* `DELETE /api/meeting/:id/` - Remover uma reserva existente

### Exemplos de requisição para criação de uma reserva de sala

```json
{
"name": "Teste"
"start": 2018-01-01 09:00:00
"end": 2018-01-01 10:00:00
"meeting_room": <id-meeting-room>
}
```
