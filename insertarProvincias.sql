INSERT INTO `provincia`(`codigo`, `nombre`) VALUES ('1','Sevilla'),('2','Cordoba'),('3','Malaga'),('4','Jaen'),('5','Almeria'),('6','Granada');
INSERT INTO `paquete`(`codigo`, `descripcion`, `destinatario`, `direccion`, `codigo_provincia`, `dni_camionero`) VALUES ('1','Paquete tecnologia','Juan Garcia','30713 Elsie Views','3','123123R'),('2','Amazon','Pablo Cortez','647 Tito Pines','1','1231231F'),('3','PcComponentes','Jose Zorrilla','23668 Gerhold Loop','4','345533433G');
INSERT INTO `conduce`(`ID`, `dni_camionero`, `matricula_camion`) VALUES ('1','345345345H','34534534G'),('2','5345345H','768867786J'),('3','64356456U','4355345345T');
INSERT INTO `camionero` (`dni`, `poblacion`, `nombre`, `telefono`, `direccion`, `salario`) VALUES ('34534534G', 'España', 'Pablo', '655675645', 'C/ Doctor Jiménez Díaz', '4000'),('1123566T', 'Francia', 'Jose', '456456T', '5522 Ethyl Coves', '2000'),('12312RF3Y', 'Alemania', 'Pan', '15541236T', '5442 Weissnat Junction', '1200');
INSERT INTO `camion` (`matricula`, `potencia`, `modelo`, `tipo`) VALUES ('6473AKG', '312cv', 'Volvo Gama FH', 'Cisterna');