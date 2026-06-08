dilemas_plan_do = [
    {
        "id": 1,
        "titulo": "El Post-it de la Vergüenza",
        "descripcion": "Detectas que el encargado de la caja tiene la contraseña del correo administrativo del abasto anotada en un Post-it pegado en el monitor. ¿Qué acción tomas?",
        "opciones": [
            {
                "texto": "Implementar un gestor de claves y dictar pauta de concientización express.",
                "impacto": {"presupuesto": -50, "seguridad_red": 25, "cultura_pyme": 20, "reputacion": 5},
                "feedback": "Gastaste un poco en la licencia, pero el personal ahora entiende el riesgo. ¡Adiós Post-it!"
            },
            {
                "texto": "Ignorarlo por ahora para no retrasar las ventas del día.",
                "impacto": {"presupuesto": 0, "seguridad_red": -20, "cultura_pyme": -10, "reputacion": 0},
                "feedback": "No gastaste dinero, pero la vulnerabilidad sigue expuesta. Cualquier cliente puede ver la clave."
            }
        ]
    },
    {
        "id": 2,
        "titulo": "CANTV Lento y Datos Móviles",
        "descripcion": "El internet local falla. Un empleado sugiere conectar la laptop de administración a su teléfono personal vía Hotspot para procesar los reportes de Pago Móvil pendientes.",
        "opciones": [
            {
                "texto": "Prohibir la conexión a redes no auditadas y esperar que retorne el servicio seguro.",
                "impacto": {"presupuesto": -20, "seguridad_red": 10, "cultura_pyme": 15, "reputacion": -5},
                "feedback": "Se retrasaron un poco las conciliaciones, pero mantuviste el perímetro de red seguro."
            },
            {
                "texto": "Permitir la conexión para no perder flujo de caja ni molestar a los clientes.",
                "impacto": {"presupuesto": 100, "seguridad_red": -30, "cultura_pyme": -15, "reputacion": 5},
                "feedback": "Procesaste los pagos, pero la laptop estuvo expuesta a tráfico móvil no cifrado. Alto riesgo de interceptación."
            }
        ]
    },
    {
        "id": 3,
        "titulo": "Actualización Crítica de Firmware",
        "descripcion": "Cisco emite una alerta sobre una vulnerabilidad crítica en el router del negocio. Parchearlo requiere apagar los sistemas de red por 20 minutos.",
        "opciones": [
            {
                "texto": "Programar el mantenimiento inmediato asumiendo la parada técnica.",
                "impacto": {"presupuesto": -40, "seguridad_red": 35, "cultura_pyme": 5, "reputacion": 10},
                "feedback": "El router quedó blindado contra exploits conocidos de día cero. La infraestructura es robusta."
            },
            {
                "texto": "Posponer la actualización para el fin de semana para evitar molestias.",
                "impacto": {"presupuesto": 0, "seguridad_red": -25, "cultura_pyme": 0, "reputacion": -10},
                "feedback": "Los sistemas siguen arriba, pero atacantes automatizados ya escanean la IP pública buscando esa falla."
            }
        ]
    }
]

ataques_aleatorios = [
    {
        "tipo": "Phishing",
        "requisito": "cultura_pyme",
        "umbral": 40,
        "exito": "Un empleado recibió un correo falso del banco solicitando coordenadas. Gracias a la capacitación, sospechó y lo reportó. ¡Ataque mitigado!",
        "fallo": "Un empleado cayó en un enlace de phishing bancario. Clonaron las credenciales y vaciaron parte de la cuenta operativa de la PYME.",
        "daño": {"presupuesto": -300, "reputacion": -20}
    },
    {
        "tipo": "Malware por USB",
        "requisito": "seguridad_red",
        "umbral": 50,
        "exito": "Colocaron un pendrive infectado en la caja, pero las políticas de restricción de puertos bloquearon la ejecución del script. ¡Salvados!",
        "fallo": "Ejecutaron un archivo infectado desde un USB. Un troyano empezó a recolectar capturas de pantalla de los inicios de sesión.",
        "daño": {"presupuesto": -150, "seguridad_red": -15, "reputacion": -15}
    }
]