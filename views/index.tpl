<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{titulo}}</title>
    <link rel="stylesheet" href="/static/bootstrap/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">{{titulo}}</h1>
        <div class="mt-4">
            <h2 class="text-center">📊 Sobre o Projeto</h2>
            <p class="text-justify">
                Este painel interativo apresenta uma visualização de dados socioeconômicos do Brasil com base em informações oficiais extraídas da <strong>API pública do IBGE</strong>. 
                Os dados são tratados com <strong>Pandas</strong>, visualizados com <strong>Matplotlib</strong> e exibidos por meio de uma aplicação web desenvolvida com o microframework <strong>Bottle</strong> em Python.
            </p>
            <p class="text-justify">
                O objetivo é fornecer uma representação gráfica clara e acessível de indicadores como: chegada de turistas internacionais, gastos em educação pública, índice de envelhecimento da população, entre outros. 
                Todo o sistema é modularizado, com separação de rotas, templates e lógica de geração de gráficos.
            </p>
            <p class="text-justify">
                Este projeto serve como exemplo de integração entre <strong>dados públicos</strong> e <strong>visualização informativa</strong> com foco em aplicações reais para análise de dados e desenvolvimento web.
            </p>
        </div>
        % if imagens:
            <div class="row">
                % for img in imagens:
                    <div class="col-md-12 text-center">
                        <img src="{{img}}" class="img-fluid" alt="Gráfico">
                    </div>
                % end
            </div>
        % else:
            <p class="text-danger text-center">Erro ao carregar dados do IBGE.</p>
        % end
    </div>
</body>
</html>
