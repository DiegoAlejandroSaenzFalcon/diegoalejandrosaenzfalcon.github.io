# SPEC — Evolución profesional del portfolio GitHub Pages

**Fecha:** 2026-09-23  
**Estado:** PROPUESTA / LISTA PARA IMPLEMENTACIÓN CONTROLADA  
**Rama:** feat/portfolio-professional-evolution-2026-09  
**Fuente de verdad transversal:** Directivas-de-Seguridad-IA, baseline 2026-09-23  
**Alcance:** únicamente el sitio público principal de identidad profesional.

## 1. Objetivo

Transformar el portfolio desde una presentación centrada principalmente en “TI/soporte” hacia una representación verificable de una trayectoria multidisciplinaria:

**Tecnología + Sistemas + Infraestructura + Automatización + Datos + IA/Agentes + Seguridad + Investigación cuantitativa + Operación real.**

No se deben inventar títulos, años de experiencia, niveles de dominio ni capacidades no demostradas.

## 2. Evidencia observada

El ecosistema público contiene, entre otros:

- `Tecnologias-de-la-Informacion`: documentación TI, MkDocs y automatización de publicación.
- `Windows-11-Professional`: administración/forensia de Windows, PowerShell, optimización, scripts, evidencia y documentación.
- `Red-Hat-Enterprise-Linux`: Linux, administración, rendimiento y hardening.
- `Automatizacion-de-Datos`: Python, automatización, documentación, CI/CD y pruebas.
- `Trading-Ciencia`: Python, investigación cuantitativa, pruebas, configuración, seguridad y reproducibilidad.
- `Soluciona-Inteligencia-Artificial`: producto aplicado, automatización, integración WhatsApp, inventario, pruebas, CI y seguridad.
- `Directivas-de-Seguridad-IA`: gobierno de agentes, seguridad, evidencia y continuidad multi-IA.
- `Vibe-Intelligence-Engine` y `Vibe-Coding-Sin-Saber-Programar`: laboratorio privado de ingeniería/agentes; no publicar contenido privado sin decisión explícita.

## 3. Arquitectura de información propuesta

Orden público:

1. Hero / propuesta profesional.
2. Evidencia de impacto y alcance.
3. Experiencia operativa real.
4. Capacidades técnicas por dominio.
5. Evolución técnica verificable.
6. Proyectos destacados.
7. Evidencia de ingeniería: Git, CI/CD, tests, documentación, seguridad.
8. Formación y certificaciones, separando estados.
9. Experiencia multidisciplinaria.
10. Contacto profesional.

## 4. Taxonomía de capacidades

### Sistemas e infraestructura
Windows, Linux/RHEL, administración, rendimiento, diagnóstico, servicios, almacenamiento, memoria, scripting.

### Redes
TCP/IP, OSI, direccionamiento, diagnóstico, infraestructura y fundamentos Cisco.

### Desarrollo y datos
Python, JavaScript, PHP, MySQL, procesamiento de datos, automatización, web.

### Automatización e IA
automatización de procesos, agentes, integración de IA, diseño de flujos, OpenCode y coordinación multi-IA.

### Ingeniería de software
Git/GitHub, ramas, PR, CI/CD, testing, linting, type checking, documentación, SDD/SSD, ADR y evidencia.

### Seguridad
hardening, Gitleaks, least privilege, higiene de secretos, seguridad de CI/CD y gobierno de agentes.

### Investigación cuantitativa
Python, análisis de datos, backtesting/investigación y metodología reproducible. No presentar resultados de trading como garantía financiera.

### Operación
logística, distribución, rutas, GPS, POS/PDA, reportes, inventario, pre-ventas, ejecución comercial y seguridad operacional.

## 5. Experiencia operacional

Debe ocupar una sección propia y no quedar relegada a una nota final.

La experiencia debe conectar operación con tecnología sin convertir cargos operativos en cargos TI.

Elementos verificables a incorporar desde la información profesional aprobada:

- Bimbo de Colombia — Conductor Entregador — agosto 2023 a 15 noviembre 2025.
- Coberturas/funciones operativas relacionadas con reportes, personal/turnos, reuniones virtuales, POS/clientes, macro entregas con pre-venta, radios/PDA, GPS y reorganización de rutas.
- ALSAM — Piscinero–Salvavidas — Girardot — hasta 11 diciembre 2025.
- Grupo Éxito — verificación de precios de competencia, reportes y macro por departamento.
- Experiencia informal de apoyo tecnológico: selección de equipos usados y configuración/traslado de información y aplicaciones en teléfono.

## 6. Evolución técnica

No usar una escala numérica de “nivel”.

Representar hitos por fecha/repositorio/evidencia. El historial Git demuestra evolución; la página debe mostrarla como trayectoria documentada.

Hitos mínimos:

- 2026-09-05 — Trading-Ciencia, primera base del framework cuantitativo.
- 2026-09-06 — Automatizacion-de-Datos, monorepo con herramientas, CI/CD y documentación.
- 2026-09-07 — Portfolio profesional inicial.
- 2026-09-12 — Windows con ingeniería de sistemas/forensia avanzada documentada en commits; Vibe-Intelligence-Engine y Vibe-Coding como laboratorio privado.
- 2026-09-23 — Soluciona IA con evolución hacia integración comercial, seguridad, pruebas e inventario; Directivas con gobernanza AICCP.

Las fechas y descripciones definitivas deben vincularse a commits concretos antes de publicar.

## 7. Proyectos

No presentar todos los repositorios con el mismo peso.

Destacados públicos:

- Soluciona Inteligencia Artificial.
- Windows 11 Professional.
- Automatización de Datos.
- Trading Ciencia.
- Red Hat Enterprise Linux.
- Tecnologías de la Información.

Directivas de Seguridad IA solo se enlazará si la decisión de visibilidad pública lo permite; actualmente es privado y el baseline prohíbe exponer contenido privado por conveniencia del portfolio.

## 8. Claims y estados

Toda afirmación técnica relevante debe poder mapearse:

CLAIM → REPOSITORIO/ARCHIVO/TEST/WORKFLOW → EVIDENCIA → STATUS.

Estados permitidos según baseline transversal:

- IMPLEMENTADO_Y_VERIFICADO
- PARCIALMENTE_IMPLEMENTADO
- PRESENTE_PERO_NO_PROBADO_E2E
- DOCUMENTADO_PERO_NO_VERIFICADO
- NO_ENCONTRADO_TRAS_INSPECCION
- DESCONOCIDO
- PLANEADO

El portfolio puede mostrar estados simplificados al público, pero nunca convertir “documentado” en “operacional” sin evidencia.

## 9. SEO y calidad técnica

Fase posterior al contenido:

- canonical.
- robots.txt.
- sitemap.xml.
- favicon.
- Open Graph/Twitter Card.
- 404.
- metadatos consistentes.
- JSON-LD coherente.
- revisión de accesibilidad.
- rendimiento y peso de assets.
- revisión de CDNs externos.
- validación de enlaces.
- revisión de privacidad de contacto.
- ubicación solo con dato confirmado por el propietario.

## 10. Seguridad del repositorio

El workflow `.github/workflows/apply-final-corrections.yml` es auto-mutante y usa `contents: write`.

No se modifica en esta SPEC sin reconstruir primero su intención/historial.

`.tmp/` y cualquier artefacto temporal se auditarán antes de eliminarse.

Objetivo posterior:

**branch → validate → PR → review → merge → deploy**

en lugar de automatización que escriba directamente sobre `main`, salvo que exista una razón documentada para conservarla.

## 11. Criterios de aceptación

- La página representa la amplitud técnica y operacional real.
- Ningún título o capacidad se exagera.
- Los proyectos se vinculan a evidencia real.
- Los repositorios privados no se exponen.
- La experiencia operacional tiene presencia visible.
- La evolución técnica se puede reconstruir mediante GitHub.
- SEO/accesibilidad/performance se validan antes de considerar terminado.
- Los cambios se realizan mediante rama + validación + PR.
- Toda decisión relevante queda versionada.
