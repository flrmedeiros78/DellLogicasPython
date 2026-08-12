# DellLogicasPython
Curso de Logica de programação em Python pela https://leadfortaleza.com.br/


Contexto
Objetivo: criar um módulo mod_xpto.py com classes e funções reutilizáveis (xpto, repartir_por_idade, um_xpto), hospedá-lo em diferentes lugares (Google Drive, GitHub, Databricks) e importá-lo a partir de um notebook consumidor (xptos.ipynb) rodando no Google Colab.
Problemas encontrados e o que cada um ensinou
1. FileNotFoundError ao abrir arquivo no Google Drive
Causa: o Google Drive não estava montado na sessão atual do Colab. Lição: a montagem do Drive (drive.mount('/content/drive')) não persiste entre sessões - precisa ser refeita sempre que o runtime reinicia.
2. NameError: name 'true' is not defined
Causa: o arquivo mod_xpto.py na verdade continha JSON ({"nbformat":4, ...}), porque tinha sido criado como "New Notebook" no Colab e só renomeado para .py. O Python tentou interpretar true (minúsculo, sintaxe JSON) como código Python, onde o correto seria True. Lição: a extensão do arquivo não determina o formato do conteúdo. Notebooks Jupyter/Colab salvam sempre em JSON por trás, independente do nome do arquivo. Um .py de verdade só existe quando criado como arquivo de texto puro (editor de código, ou "New File" no painel de arquivos).
3. ModuleNotFoundError: No module named 'X'
Causa: atraso de sincronização do Google Drive - o arquivo existia, mas ainda não estava visível para o sistema de arquivos do Colab no momento do import. Lição: ao trabalhar com armazenamento montado (Drive, buckets, etc.), pode haver latência entre "arquivo criado" e "arquivo disponível". Vale checar com os.listdir() ou glob antes de importar.
4. Confusão entre nome do módulo e alias
import mod_xpto_v3 as xpto
from xpto import xpto   # ❌ erro: 'xpto' não é o nome real do módulo
Lição: as xpto cria só um apelido local. O nome do arquivo (mod_xpto_v3) continua sendo o único nome válido para from ... import .... Ou se usa import X as Y (e depois Y.funcao()), ou se usa from X import funcao - não misturar os dois esperando que o alias funcione nas duas formas.
5. ImportError: cannot import name 'xpto' from 'mod_xpto_v3'
Causa: mesmo problema do item 2, mas em uma versão posterior do arquivo - criado de novo como notebook disfarçado de .py. Lição: reforça que o erro de formato (notebook vs. .py puro) pode se repetir sempre que o arquivo for recriado pela interface errada. Vale ter o hábito de inspecionar o conteúdo bruto do arquivo (open(...).read()) quando um import falha de forma inesperada.
6. Cache de imports (sys.modules)
Lição: o Python só lê um módulo do disco na primeira vez que ele é importado na sessão. Edições posteriores ao arquivo não são recarregadas automaticamente. Soluções:
Reiniciar o runtime/kernel (mais simples e confiável)
Ou remover manualmente do cache: del sys.modules['nome_do_modulo'] (atenção: é sys.modules, no plural, não sys.module)
7. Baixar arquivo do GitHub via wget/urllib trazendo HTML em vez do código
Causa: uso da URL da página de visualização do GitHub (github.com/usuario/repo/blob/main/arquivo.py) em vez da URL do conteúdo puro. Lição: para baixar o conteúdo real de um arquivo hospedado no GitHub, usar sempre o link raw (raw.githubusercontent.com/usuario/repo/main/arquivo.py), acessível pelo botão "Raw" na interface do GitHub.
Resumo - regras práticas para módulos Python reutilizáveis
1.Crie arquivos .py de módulo em um editor de texto puro (VS Code, "New File"), nunca via "New Notebook" renomeado.
2.Para importar por alias, seja consistente: import X as Y → use sempre Y.funcao().
3.Depois de editar um módulo já importado, reinicie a sessão antes de testar de novo.
4.Ao baixar arquivos de repositórios remotos, use sempre a URL de conteúdo puro (raw), nunca a URL da página web.
5.Quando um import falhar de forma inesperada, inspecione o conteúdo bruto do arquivo antes de assumir que é um problema de caminho ou de nome.

Módulo de exemplo: mod_xpto.py - classes e funções relacionadas a xptos, usado para praticar organização de código em módulos reutilizáveis no ecossistema Python (Colab, GitHub, Databricks).