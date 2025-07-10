<?php
if (php_sapi_name() == 'cli-server') {
    $urlPath = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);
    $segments = explode('/', trim($urlPath, '/'));

    if (count($segments) === 3) {
        list($operacao, $num1, $num2) = $segments;

        switch ($operacao) {
            case 'somar':
                $resultado = $num1 + $num2;
                break;
            case 'subtrair':
                $resultado = $num1 - $num2;
                break;
            case 'multiplicar':
                $resultado = $num1 * $num2;
                break;
            case 'dividir':
                if ($num2 == 0) {
                    $resultado = "Erro: divisão por zero";
                } else {
                    $resultado = $num1 / $num2;
                }
                break;
            default:
                header("HTTP/1.1 404 Not Found");
                echo "Operação inválida";
                exit;
        }
        header('Content-Type: text/plain');
        echo $resultado;
        exit;
    }

    $file = __DIR__ . $urlPath;
    if (is_file($file)) {
        return false; // Serve arquivo estático normalmente
    }
}

// Para qualquer outra requisição inválida
header("HTTP/1.1 404 Not Found");
echo "Rota inválida";
