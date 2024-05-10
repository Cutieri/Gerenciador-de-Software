def IpValidator(ip: str):
    # Remove os pontos do texto para poder testar se a string só contém números
    ipStringWithoutDots = ip.replace(".", '')

    # Testa se a string o ip contém apenas números
    isIpStringNumberOnly = ipStringWithoutDots.isdigit()

    if not(isIpStringNumberOnly):
        raise Exception("Enderço de IP Invalido, motivo: endereço de ip precisa conter apenas numeros")

    # Divide a string nos pontos - 123.123.123.123 -> ["123", "123", "123", "123"]
    ipParts = ip.split(".")

    # Caso o ip não contenha as 4 partes necessárias ele levanta um erro.
    if(ipParts.__len__() != 4):
        raise Exception("Enderço de IP Invalido, motivo: endereço de ip precisa ter 4 partes")
    
    for part in ipParts:
        isIpNumberValid = int(part) > 0 and int(part) < 255

        # Se o número for menor que 0 ou maior que 255 ele levanta um erro. 
        if not (isIpNumberValid):
            raise Exception("Enderço de IP Invalido, motivo: numeros do ip precisam estar entre 0 e 255")
            
    return str