#!/bin/bash
fecha=`date +%Y%m%d%H%M%S`
echo "Content-Type: text/plain"
echo

casa="../../compile"

cat | dd count=1 bs=1M  >  ../upload/$fecha.ts

if [[ `grep "Llave para la librería CryptoJS" ../upload/$fecha.ts` != ""  ]]; then
#    echo -e "\nArchivo correcto. Espere archivo cerca de 1 minuto. "
#    echo "Código de petición: $fecha"
     echo "$fecha"
     $casa/bin/compile_front  $fecha &> $casa/log/$fecha.log &
#    while ! [ -f ../descargas/$fecha.tgz ] ; do
#        echo  "#"
#	sleep 5
#    done
#    rm -f ../upload/$fecha.ts
    exit 0
else
    echo "Archivo incorrecto"  
    rm -f ../upload/$fecha.ts
    exit 1
fi

