---
titulo: wiki
area: conhecimento
fase: em uso
revisado_em: 2026-10-04
---

## Notas
Em 2026-09-29 o curso de AQFT foi republicado a partir do dossiê de aulas corrigido, com os links do wiki restaurados, depois da checagem de privacidade em content/ e public/. Mais tarde no mesmo dia, as dezoito páginas do curso tocadas pela primeira passagem da revisão de clareza, pedagogia e correção foram republicadas, de novo depois da checagem de privacidade.

Em 2026-09-30 a página do conceito Bell-CHSH foi republicada com o argumento corrigido do limite local, depois da checagem de privacidade em content/ e public/. A sincronização partiu de uma cópia do commit do vault, para que mudanças ainda não commitadas de outras sessões não fossem ao site.

Em 2026-10-01 o curso de AdS/CFT foi republicado com o novo título, *Holography through Quantum Information and Operator Algebras*: as 32 aulas, o programa, as convenções e os apêndices do dossiê, com as figuras de `courses/ads-cft-course/assets`, que entrou na lista PUBLISH. As trinta notas semanais antigas saíram do site. O `cull-links.py` passou a levar os links do vault escritos a partir da raiz (`wiki/courses/...`) aos caminhos do site, o que também consertou sete links quebrados das páginas de redes neurais. A checagem de privacidade em content/ e public/ não achou nada novo, e a sincronização partiu de uma cópia do commit do vault. O `~/Projects/physics-wiki` local ainda está antes desse commit, e sincronizar a partir dele traria o curso antigo de volta.

Em 2026-10-04 o curso de simetrias generalizadas foi republicado com a edição completa do dossiê, sincronizada de um clone do commit e299cbd do vault: as trinta notas menos a Semana 14 do Semestre II, que segue em detalhe o manuscrito do grupo ainda não submetido e entrou no EXCLUDE do `sync-wiki.sh` até o manuscrito ser público. A construção local não acusou erro de KaTeX nem tabela quebrada; quatro trechos que renderizavam mal foram corrigidos antes no dossiê. A checagem de privacidade em content/ e public/ não achou nada novo. O `~/Projects/physics-wiki` local estava atrás do GitHub e guardava edições de 21/09 não commitadas. Ainda no mesmo dia foram republicadas, de um clone do commit 0bc14e3, as quatro páginas que descreviam a versão anterior do manuscrito (condensation-defects, villain-action, higher-form-symmetries e a área confinement-duality), sem nada novo na checagem de privacidade.

Ainda em 2026-10-04 as edições de 21/09, a ingestão do artigo de Witten sobre a função de Chern–Simons e o efeito Hall quântico, foram corrigidas e integradas ao vault (d1db86e), e o `~/Projects/physics-wiki` local foi posto em dia com o GitHub; o `sync-wiki.sh` sem argumento volta a sincronizar a versão atual. As páginas dessa ingestão foram publicadas no mesmo dia, sincronizadas de um clone do commit d1db86e, sem nada novo na checagem de privacidade e sem erro na construção local.
