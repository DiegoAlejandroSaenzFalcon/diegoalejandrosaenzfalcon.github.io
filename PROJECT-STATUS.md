# PROJECT-STATUS.md

## Estado

**VERIFIED / EVIDENCED / DOCUMENTED — auditoría de repositorio**

Fecha de cierre: 2026-10-06

## Alcance

Auditoría repository-level del portafolio público de GitHub Pages:

- contenido público y propósito del repositorio;
- autoridad y reglas para agentes;
- política de seguridad/publicación;
- referencias obsoletas de gobierno;
- enlaces de autoridad;
- secretos evidentes mediante búsqueda de patrones;
- PRs paralelos/obsoletos;
- coherencia básica del contenido público.

## Hallazgos corregidos

1. Se corrigió la ubicación pública del portafolio a **Girardot, Cundinamarca, Colombia** donde aparecía la ubicación anterior.
2. Se sustituyó la referencia pública obsoleta a `Directivas-de-Seguridad-IA` por el repositorio canónico actual `Directivas-de-Seguridad`.
3. Se mantuvo `AGENTS.md` como instrucción local y `SECURITY.md` como política pública, ambos subordinados a la autoridad transversal de `Directivas-de-Seguridad`.
4. Se cerraron PR #6 y PR #7 como trabajo paralelo superseded. No se fusionó código de esos PR.
5. Se verificó que no existen en el árbol principal los mecanismos inseguros de `HONEYTOKEN.md`, ni referencias indexadas a secretos comunes o a autoridades obsoletas mediante las búsquedas realizadas.

## Autoauditoría del trabajo

Durante la revisión interna se detectó y corrigió una afirmación incorrecta de estado académico (`En curso` → `Aplazada`) y se suavizaron etiquetas de credenciales que podían implicar una verificación externa no realizada durante esta auditoría. Esto queda registrado para no confundir contenido publicado con evidencia independiente.

## Autoauditoría adicional

Se detectó una segunda inconsistencia de publicación: el bloque estructurado `schema.org` de `index.html` conservaba Bogotá como ubicación mientras el contenido visible del portafolio indicaba Girardot. Se corrigió a Girardot, Cundinamarca, Colombia.

## Evidencia

- PR #8: baseline de gobierno público, fusionado antes del cierre.
- Commits de corrección de contenido: `95aae721c5000e0d4ba27f196758b99a8de74199` y `dbf731273552f156d5582717c4c2460c44f4733a`.
- PR #6: cerrado como superseded.
- PR #7: cerrado como superseded.
- Estado actual de la rama auditada: `main`. La corrección de autoauditoría adicional se registrará en el commit de cierre de esta revisión.

## Límites de esta auditoría

Esta auditoría no afirma:

- que el navegador externo haya renderizado cada recurso remoto correctamente;
- que cada enlace externo de terceros permanezca disponible;
- que GitHub Pages haya ejecutado un pipeline de Actions, porque este repositorio actualmente no contiene un workflow de Pages/CI en `main`;
- que una búsqueda de patrones equivalga a una auditoría criptográfica o histórica completa de todos los commits.

## Clasificación

**Portfolio / educación / presentación pública.**

El repositorio es una superficie pública de presentación. No es fuente de autoridad técnica ni contiene la gobernanza completa de la organización.

## Regla de continuidad

Cualquier cambio futuro debe volver a verificar contenido público, enlaces, credenciales, datos personales publicados deliberadamente, referencias de autoridad y seguridad antes de publicación.
