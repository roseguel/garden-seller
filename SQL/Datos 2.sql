--------------------------------------------------------
-- Archivo creado  - miércoles-junio-29-2022   
--------------------------------------------------------
REM INSERTING into BUYBEE.AUTH_GROUP
SET DEFINE OFF;
REM INSERTING into BUYBEE.AUTH_GROUP_PERMISSIONS
SET DEFINE OFF;
REM INSERTING into BUYBEE.AUTH_PERMISSION
SET DEFINE OFF;
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('1','Can add log entry','1','add_logentry');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('2','Can change log entry','1','change_logentry');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('3','Can delete log entry','1','delete_logentry');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('4','Can view log entry','1','view_logentry');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('5','Can add permission','2','add_permission');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('6','Can change permission','2','change_permission');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('7','Can delete permission','2','delete_permission');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('8','Can view permission','2','view_permission');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('9','Can add group','3','add_group');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('10','Can change group','3','change_group');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('11','Can delete group','3','delete_group');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('12','Can view group','3','view_group');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('13','Can add user','4','add_user');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('14','Can change user','4','change_user');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('15','Can delete user','4','delete_user');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('16','Can view user','4','view_user');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('17','Can add content type','5','add_contenttype');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('18','Can change content type','5','change_contenttype');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('19','Can delete content type','5','delete_contenttype');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('20','Can view content type','5','view_contenttype');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('21','Can add session','6','add_session');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('22','Can change session','6','change_session');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('23','Can delete session','6','delete_session');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('24','Can view session','6','view_session');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('25','Can add carrito','7','add_carrito');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('26','Can change carrito','7','change_carrito');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('27','Can delete carrito','7','delete_carrito');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('28','Can view carrito','7','view_carrito');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('29','Can add categoria','8','add_categoria');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('30','Can change categoria','8','change_categoria');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('31','Can delete categoria','8','delete_categoria');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('32','Can view categoria','8','view_categoria');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('33','Can add estado envio','9','add_estadoenvio');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('34','Can change estado envio','9','change_estadoenvio');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('35','Can delete estado envio','9','delete_estadoenvio');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('36','Can view estado envio','9','view_estadoenvio');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('37','Can add estado pedido','10','add_estadopedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('38','Can change estado pedido','10','change_estadopedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('39','Can delete estado pedido','10','delete_estadopedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('40','Can view estado pedido','10','view_estadopedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('41','Can add usuario','11','add_usuario');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('42','Can change usuario','11','change_usuario');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('43','Can delete usuario','11','delete_usuario');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('44','Can view usuario','11','view_usuario');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('45','Can add producto venta','12','add_productoventa');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('46','Can change producto venta','12','change_productoventa');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('47','Can delete producto venta','12','delete_productoventa');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('48','Can view producto venta','12','view_productoventa');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('49','Can add producto imagen','13','add_productoimagen');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('50','Can change producto imagen','13','change_productoimagen');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('51','Can delete producto imagen','13','delete_productoimagen');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('52','Can view producto imagen','13','view_productoimagen');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('53','Can add producto carrito','14','add_productocarrito');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('54','Can change producto carrito','14','change_productocarrito');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('55','Can delete producto carrito','14','delete_productocarrito');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('56','Can view producto carrito','14','view_productocarrito');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('57','Can add pedido','15','add_pedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('58','Can change pedido','15','change_pedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('59','Can delete pedido','15','delete_pedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('60','Can view pedido','15','view_pedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('61','Can add envio','16','add_envio');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('62','Can change envio','16','change_envio');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('63','Can delete envio','16','delete_envio');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('64','Can view envio','16','view_envio');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('65','Can add detalle pedido','17','add_detallepedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('66','Can change detalle pedido','17','change_detallepedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('67','Can delete detalle pedido','17','delete_detallepedido');
Insert into BUYBEE.AUTH_PERMISSION (ID,NAME,CONTENT_TYPE_ID,CODENAME) values ('68','Can view detalle pedido','17','view_detallepedido');
REM INSERTING into BUYBEE.AUTH_USER
SET DEFINE OFF;
Insert into BUYBEE.AUTH_USER (ID,PASSWORD,LAST_LOGIN,IS_SUPERUSER,USERNAME,FIRST_NAME,LAST_NAME,EMAIL,IS_STAFF,IS_ACTIVE,DATE_JOINED) values ('1','pbkdf2_sha256$320000$rDrjWBfbZt7wsFa5yvkC1U$Ca+RuzkUkwjVylfcSlvIbxX/QO/cH90LDnBbzrqJ8qk=',to_timestamp('27-06-22 04.22.58.412065000 AM','DD-MM-RR HH.MI.SSXFF AM'),'1','admin',null,null,null,'1','1',to_timestamp('26-06-22 03.37.34.837888000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.AUTH_USER (ID,PASSWORD,LAST_LOGIN,IS_SUPERUSER,USERNAME,FIRST_NAME,LAST_NAME,EMAIL,IS_STAFF,IS_ACTIVE,DATE_JOINED) values ('3','pbkdf2_sha256$320000$0hSRS9s7jPyzvGo0Y6TnxT$KyKLr1cBfhNhK9AGx2/EtSlb4VdLoZxzCC00oxFxsCA=',to_timestamp('27-06-22 06.24.49.290715000 PM','DD-MM-RR HH.MI.SSXFF AM'),'0','Alexis',null,null,'alexis@gmail.com','0','1',to_timestamp('27-06-22 12.24.48.188893000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.AUTH_USER (ID,PASSWORD,LAST_LOGIN,IS_SUPERUSER,USERNAME,FIRST_NAME,LAST_NAME,EMAIL,IS_STAFF,IS_ACTIVE,DATE_JOINED) values ('2','pbkdf2_sha256$320000$p6Y2ziVJ6jpmacs41rZkYt$T1DFjnlQergm8BCpmLzuzzh28MM13dN4+l9XDiDFleg=',to_timestamp('28-06-22 12.30.08.632370000 AM','DD-MM-RR HH.MI.SSXFF AM'),'0','Ariel',null,null,'redthelegendarytrainer@gmail.com','0','1',to_timestamp('26-06-22 03.41.50.338980000 AM','DD-MM-RR HH.MI.SSXFF AM'));
REM INSERTING into BUYBEE.AUTH_USER_GROUPS
SET DEFINE OFF;
REM INSERTING into BUYBEE.AUTH_USER_USER_PERMISSIONS
SET DEFINE OFF;
REM INSERTING into BUYBEE.BUYBEEAPP_CARRITO
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_CARRITO (ID,TOTAL,CUPON,DUENIO_ID) values ('2','0',null,'209197229');
Insert into BUYBEE.BUYBEEAPP_CARRITO (ID,TOTAL,CUPON,DUENIO_ID) values ('1','0',null,'209197219');
REM INSERTING into BUYBEE.BUYBEEAPP_CATEGORIA
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_CATEGORIA (ID,NOMBRE,FOTO) values ('1','Cactáceas','categorias/cactaceo.jpg');
Insert into BUYBEE.BUYBEEAPP_CATEGORIA (ID,NOMBRE,FOTO) values ('2','Flores Hogareñas','categorias/flor-hogareñas.jpg');
Insert into BUYBEE.BUYBEEAPP_CATEGORIA (ID,NOMBRE,FOTO) values ('3','Flor Silvestre','categorias/flor-silvestre.jpg');
Insert into BUYBEE.BUYBEEAPP_CATEGORIA (ID,NOMBRE,FOTO) values ('4','Árbol Silvestre','categorias/arbol-silvestre.jpg');
Insert into BUYBEE.BUYBEEAPP_CATEGORIA (ID,NOMBRE,FOTO) values ('5','Árboles Frutales','categorias/arboles_frutales.jpg');
Insert into BUYBEE.BUYBEEAPP_CATEGORIA (ID,NOMBRE,FOTO) values ('6','Árboles Pequeños','categorias/arboles-pequeños.jpg');
Insert into BUYBEE.BUYBEEAPP_CATEGORIA (ID,NOMBRE,FOTO) values ('7','Hongos','categorias/hongos.jpg');
Insert into BUYBEE.BUYBEEAPP_CATEGORIA (ID,NOMBRE,FOTO) values ('8','Semillas','categorias/semillas.jpg');
REM INSERTING into BUYBEE.BUYBEEAPP_DETALLEPEDIDO
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_DETALLEPEDIDO (ID,CANTIDAD,SUBTOTAL,PEDIDO_ID,PRODUCTO_ID) values ('1','1','6990','1','1');
Insert into BUYBEE.BUYBEEAPP_DETALLEPEDIDO (ID,CANTIDAD,SUBTOTAL,PEDIDO_ID,PRODUCTO_ID) values ('2','1','4990','1','4');
Insert into BUYBEE.BUYBEEAPP_DETALLEPEDIDO (ID,CANTIDAD,SUBTOTAL,PEDIDO_ID,PRODUCTO_ID) values ('30','1','6990','29','1');
Insert into BUYBEE.BUYBEEAPP_DETALLEPEDIDO (ID,CANTIDAD,SUBTOTAL,PEDIDO_ID,PRODUCTO_ID) values ('31','1','4990','29','5');
Insert into BUYBEE.BUYBEEAPP_DETALLEPEDIDO (ID,CANTIDAD,SUBTOTAL,PEDIDO_ID,PRODUCTO_ID) values ('32','1','9990','30','2');
Insert into BUYBEE.BUYBEEAPP_DETALLEPEDIDO (ID,CANTIDAD,SUBTOTAL,PEDIDO_ID,PRODUCTO_ID) values ('28','1','4990','29','4');
Insert into BUYBEE.BUYBEEAPP_DETALLEPEDIDO (ID,CANTIDAD,SUBTOTAL,PEDIDO_ID,PRODUCTO_ID) values ('29','1','49990','29','6');
Insert into BUYBEE.BUYBEEAPP_DETALLEPEDIDO (ID,CANTIDAD,SUBTOTAL,PEDIDO_ID,PRODUCTO_ID) values ('33','1','19990','31','21');
REM INSERTING into BUYBEE.BUYBEEAPP_ENVIO
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_ENVIO (ID,FECHA_EMISION,FECHA_ACTUALIZACION,COMPRADOR_ID,ESTADO_ID,PEDIDO_ID,VENDEDOR_ID) values ('1',to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'209197229','2','1','209197219');
Insert into BUYBEE.BUYBEEAPP_ENVIO (ID,FECHA_EMISION,FECHA_ACTUALIZACION,COMPRADOR_ID,ESTADO_ID,PEDIDO_ID,VENDEDOR_ID) values ('2',to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'209197229','1','2','209197219');
Insert into BUYBEE.BUYBEEAPP_ENVIO (ID,FECHA_EMISION,FECHA_ACTUALIZACION,COMPRADOR_ID,ESTADO_ID,PEDIDO_ID,VENDEDOR_ID) values ('26',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'209197229','1','30','209197219');
Insert into BUYBEE.BUYBEEAPP_ENVIO (ID,FECHA_EMISION,FECHA_ACTUALIZACION,COMPRADOR_ID,ESTADO_ID,PEDIDO_ID,VENDEDOR_ID) values ('27',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'209197229','1','31','209197219');
Insert into BUYBEE.BUYBEEAPP_ENVIO (ID,FECHA_EMISION,FECHA_ACTUALIZACION,COMPRADOR_ID,ESTADO_ID,PEDIDO_ID,VENDEDOR_ID) values ('28',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'209197229','1','32','209197219');
Insert into BUYBEE.BUYBEEAPP_ENVIO (ID,FECHA_EMISION,FECHA_ACTUALIZACION,COMPRADOR_ID,ESTADO_ID,PEDIDO_ID,VENDEDOR_ID) values ('24',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'209197229','1','28','209197219');
Insert into BUYBEE.BUYBEEAPP_ENVIO (ID,FECHA_EMISION,FECHA_ACTUALIZACION,COMPRADOR_ID,ESTADO_ID,PEDIDO_ID,VENDEDOR_ID) values ('25',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'209197229','1','29','209197219');
Insert into BUYBEE.BUYBEEAPP_ENVIO (ID,FECHA_EMISION,FECHA_ACTUALIZACION,COMPRADOR_ID,ESTADO_ID,PEDIDO_ID,VENDEDOR_ID) values ('29',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'209197219','1','33','209197229');
REM INSERTING into BUYBEE.BUYBEEAPP_ESTADOENVIO
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_ESTADOENVIO (ID,NOMBRE) values ('1','En espera');
Insert into BUYBEE.BUYBEEAPP_ESTADOENVIO (ID,NOMBRE) values ('2','Enviado');
Insert into BUYBEE.BUYBEEAPP_ESTADOENVIO (ID,NOMBRE) values ('3','Cancelado');
Insert into BUYBEE.BUYBEEAPP_ESTADOENVIO (ID,NOMBRE) values ('4','Recibido');
REM INSERTING into BUYBEE.BUYBEEAPP_ESTADOPEDIDO
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_ESTADOPEDIDO (ID,NOMBRE) values ('1','Procesado');
Insert into BUYBEE.BUYBEEAPP_ESTADOPEDIDO (ID,NOMBRE) values ('2','Cancelado');
REM INSERTING into BUYBEE.BUYBEEAPP_PEDIDO
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_PEDIDO (ID,FECHA,TOTAL,COMPRADOR_ID,ESTADO_ID) values ('1',to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'11980','209197229','1');
Insert into BUYBEE.BUYBEEAPP_PEDIDO (ID,FECHA,TOTAL,COMPRADOR_ID,ESTADO_ID) values ('30',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'9990','209197229','1');
Insert into BUYBEE.BUYBEEAPP_PEDIDO (ID,FECHA,TOTAL,COMPRADOR_ID,ESTADO_ID) values ('29',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'66960','209197229','1');
Insert into BUYBEE.BUYBEEAPP_PEDIDO (ID,FECHA,TOTAL,COMPRADOR_ID,ESTADO_ID) values ('31',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'19990','209197219','1');
REM INSERTING into BUYBEE.BUYBEEAPP_PRODUCTOCARRITO
SET DEFINE OFF;
REM INSERTING into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('3','productosImagenes/imagen_2022-05-26_233903520_9zJnpoB.png','1');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('4','productosImagenes/imagen_2022-05-27_184519356_lJ6y91K.png','1');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('5','productosImagenes/imagen_2022-05-27_184535584_RpnpwGp.png','1');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('6','productosImagenes/imagen_2022-05-27_184559772_vTPHaFH.png','1');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('7','productosImagenes/imagen_2022-05-26_234037289_7WIF1WO.png','2');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('8','productosImagenes/imagen_2022-05-26_233618582_MEvVZ33.png','3');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('9','productosImagenes/imagen_2022-05-31_182350025_WX93YHb.png','4');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('10','productosImagenes/imagen_2022-05-31_182400713_8ZKQuCh.png','4');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('11','productosImagenes/imagen_2022-05-31_182417228_b6X7NrZ.png','4');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('12','productosImagenes/imagen_2022-05-31_182215351_0TpqDFe.png','5');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('13','productosImagenes/imagen_2022-05-31_182231236_n60QelL.png','5');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('14','productosImagenes/imagen_2022-05-31_182242839_EVANVX2.png','5');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('21','productosImagenes/8a5629bb67aaf0bcd103a2aa12fcbaa2c8b632e3_original.jpeg','21');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOIMAGEN (ID,IMAGEN,PRODUCTO_ID) values ('15','productosImagenes/imagen_2022-06-26_171324565.png','6');
REM INSERTING into BUYBEE.BUYBEEAPP_PRODUCTOVENTA
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_PRODUCTOVENTA (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,FECHA_PUBLICACION,VISTAS,COMPRAS,CATEGORIA_ID,VENDEDOR_ID) values ('1','Hongo Café','Ricos Hongos Cafés, perfectos para la preparación de comidas.','6990','39',to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'24','0','7','209197219');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOVENTA (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,FECHA_PUBLICACION,VISTAS,COMPRAS,CATEGORIA_ID,VENDEDOR_ID) values ('2','Hongo Marino','Rico hongo marino, extraído de la playa de Talcahuano.','9990','44',to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'3','1','7','209197219');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOVENTA (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,FECHA_PUBLICACION,VISTAS,COMPRAS,CATEGORIA_ID,VENDEDOR_ID) values ('3','Hongo Rojo','Rico hongo rojo, extraído de las profundidades del Bosque Tumbes.','19990','4',to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'2','0','7','209197219');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOVENTA (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,FECHA_PUBLICACION,VISTAS,COMPRAS,CATEGORIA_ID,VENDEDOR_ID) values ('4','Cactus','Lindo cactus pequeño, perfecto para adornar un living room.
Macetero no incluído.','4990','30',to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'48','0','1','209197219');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOVENTA (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,FECHA_PUBLICACION,VISTAS,COMPRAS,CATEGORIA_ID,VENDEDOR_ID) values ('5','Flor de Cactus','Linda flor de cactus, perfecto para adornar superficies.
Macetas no incluídas.','4990','39',to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'9','0','1','209197219');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOVENTA (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,FECHA_PUBLICACION,VISTAS,COMPRAS,CATEGORIA_ID,VENDEDOR_ID) values ('21','Bonsai Sakura','Lindo árbol Bonsai de Sakura. Es real y viene con su macetero e instrucciones de cuidado.','19990','39',to_date('27-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'8','1','6','209197229');
Insert into BUYBEE.BUYBEEAPP_PRODUCTOVENTA (ID,NOMBRE,DESCRIPCION,PRECIO,STOCK,FECHA_PUBLICACION,VISTAS,COMPRAS,CATEGORIA_ID,VENDEDOR_ID) values ('6','Naranjo Pequeño','Lindo árbol de naranjas pequeño, perfecto para comenzar a plantar.','49990','30',to_date('26-06-22 00:00:00','DD-MM-RR HH24:MI:SS'),'6','0','5','209197219');
REM INSERTING into BUYBEE.BUYBEEAPP_USUARIO
SET DEFINE OFF;
Insert into BUYBEE.BUYBEEAPP_USUARIO (RUT,NOMBREUSUARIO,NOMBRES,APELLIDOS,EMAIL,NUMERO,FOTO_PERFIL,SUSCRITO) values ('209197229','Alexis','Alexis Ariel','Silva Rivera','alexis@gmail.com',null,'fotosPerfil/imagen_2022-06-26_202618799.png','0');
Insert into BUYBEE.BUYBEEAPP_USUARIO (RUT,NOMBREUSUARIO,NOMBRES,APELLIDOS,EMAIL,NUMERO,FOTO_PERFIL,SUSCRITO) values ('209197219','Ariel','Ariel Alexis','Silva Rivera','redthelegendarytrainer@gmail.com',null,'fotosPerfil/imagen_2022-06-25_234217349.png','1');
REM INSERTING into BUYBEE.DJANGO_ADMIN_LOG
SET DEFINE OFF;
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('9',to_timestamp('27-06-22 12.52.59.686033000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Procesado','1','10','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('10',to_timestamp('27-06-22 12.53.07.424294000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Cancelado','1','10','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('11',to_timestamp('27-06-22 12.53.29.304248000 AM','DD-MM-RR HH.MI.SSXFF AM'),'En espera','1','9','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('12',to_timestamp('27-06-22 12.57.27.576395000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Rechazado','1','9','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('13',to_timestamp('27-06-22 12.57.47.891388000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Cancelado','1','9','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('14',to_timestamp('27-06-22 12.57.55.844179000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Enviado','2','9','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('15',to_timestamp('27-06-22 12.58.00.659365000 AM','DD-MM-RR HH.MI.SSXFF AM'),'En destino','1','9','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('16',to_timestamp('27-06-22 01.01.07.291327000 AM','DD-MM-RR HH.MI.SSXFF AM'),'1','1','15','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('17',to_timestamp('27-06-22 01.01.41.087969000 AM','DD-MM-RR HH.MI.SSXFF AM'),'1','1','17','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('18',to_timestamp('27-06-22 01.01.52.164920000 AM','DD-MM-RR HH.MI.SSXFF AM'),'6990','1','17','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('19',to_timestamp('27-06-22 01.33.34.056291000 AM','DD-MM-RR HH.MI.SSXFF AM'),'1','1','16','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('20',to_timestamp('27-06-22 01.33.42.251043000 AM','DD-MM-RR HH.MI.SSXFF AM'),'2','1','16','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('21',to_timestamp('27-06-22 01.38.01.953530000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Recibido','2','9','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('1',to_timestamp('26-06-22 03.39.35.935275000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Cactáceas','1','8','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('2',to_timestamp('26-06-22 03.39.53.656080000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Flores Hogareñas','1','8','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('3',to_timestamp('26-06-22 03.40.08.466201000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Flor Silvestre','1','8','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('4',to_timestamp('26-06-22 03.40.21.286060000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Árbol Silvestre','1','8','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('5',to_timestamp('26-06-22 03.40.35.177509000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Árboles Frutales','1','8','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('6',to_timestamp('26-06-22 03.40.48.887730000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Árboles Pequeños','1','8','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('7',to_timestamp('26-06-22 03.40.59.266543000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Hongos','1','8','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('8',to_timestamp('26-06-22 03.41.08.315194000 AM','DD-MM-RR HH.MI.SSXFF AM'),'Semillas','1','8','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('22',to_timestamp('27-06-22 04.23.14.862265000 AM','DD-MM-RR HH.MI.SSXFF AM'),'2','2','17','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('23',to_timestamp('27-06-22 04.23.35.662309000 AM','DD-MM-RR HH.MI.SSXFF AM'),'2','2','17','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('24',to_timestamp('27-06-22 04.23.40.771786000 AM','DD-MM-RR HH.MI.SSXFF AM'),'1','2','17','1');
Insert into BUYBEE.DJANGO_ADMIN_LOG (ID,ACTION_TIME,OBJECT_REPR,ACTION_FLAG,CONTENT_TYPE_ID,USER_ID) values ('25',to_timestamp('27-06-22 04.23.54.667040000 AM','DD-MM-RR HH.MI.SSXFF AM'),'2','2','17','1');
REM INSERTING into BUYBEE.DJANGO_CONTENT_TYPE
SET DEFINE OFF;
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('1','admin','logentry');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('2','auth','permission');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('3','auth','group');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('4','auth','user');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('5','contenttypes','contenttype');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('6','sessions','session');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('7','BuyBeeApp','carrito');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('8','BuyBeeApp','categoria');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('9','BuyBeeApp','estadoenvio');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('10','BuyBeeApp','estadopedido');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('11','BuyBeeApp','usuario');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('12','BuyBeeApp','productoventa');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('13','BuyBeeApp','productoimagen');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('14','BuyBeeApp','productocarrito');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('15','BuyBeeApp','pedido');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('16','BuyBeeApp','envio');
Insert into BUYBEE.DJANGO_CONTENT_TYPE (ID,APP_LABEL,MODEL) values ('17','BuyBeeApp','detallepedido');
REM INSERTING into BUYBEE.DJANGO_MIGRATIONS
SET DEFINE OFF;
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('1','BuyBeeApp','0001_initial',to_timestamp('26-06-22 03.35.14.949852000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('2','BuyBeeApp','0002_alter_envio_pedido',to_timestamp('26-06-22 03.35.16.992190000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('3','contenttypes','0001_initial',to_timestamp('26-06-22 03.35.17.035200000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('4','auth','0001_initial',to_timestamp('26-06-22 03.35.17.557100000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('5','admin','0001_initial',to_timestamp('26-06-22 03.35.17.912292000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('6','admin','0002_logentry_remove_auto_add',to_timestamp('26-06-22 03.35.17.938298000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('7','admin','0003_logentry_add_action_flag_choices',to_timestamp('26-06-22 03.35.17.964305000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('8','contenttypes','0002_remove_content_type_name',to_timestamp('26-06-22 03.35.18.921280000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('9','auth','0002_alter_permission_name_max_length',to_timestamp('26-06-22 03.35.19.015274000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('10','auth','0003_alter_user_email_max_length',to_timestamp('26-06-22 03.35.19.050282000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('11','auth','0004_alter_user_username_opts',to_timestamp('26-06-22 03.35.19.077288000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('12','auth','0005_alter_user_last_login_null',to_timestamp('26-06-22 03.35.19.109299000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('13','auth','0006_require_contenttypes_0002',to_timestamp('26-06-22 03.35.19.133328000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('14','auth','0007_alter_validators_add_error_messages',to_timestamp('26-06-22 03.35.19.162335000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('15','auth','0008_alter_user_username_max_length',to_timestamp('26-06-22 03.35.19.212395000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('16','auth','0009_alter_user_last_name_max_length',to_timestamp('26-06-22 03.35.19.243402000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('17','auth','0010_alter_group_name_max_length',to_timestamp('26-06-22 03.35.19.278410000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('18','auth','0011_update_proxy_permissions',to_timestamp('26-06-22 03.35.19.309418000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('19','auth','0012_alter_user_first_name_max_length',to_timestamp('26-06-22 03.35.19.340423000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('20','sessions','0001_initial',to_timestamp('26-06-22 03.35.19.424276000 AM','DD-MM-RR HH.MI.SSXFF AM'));
Insert into BUYBEE.DJANGO_MIGRATIONS (ID,APP,NAME,APPLIED) values ('21','BuyBeeApp','0003_remove_detallepedido_producto_detallepedido_producto',to_timestamp('27-06-22 04.22.37.515191000 AM','DD-MM-RR HH.MI.SSXFF AM'));
REM INSERTING into BUYBEE.DJANGO_SESSION
SET DEFINE OFF;
Insert into BUYBEE.DJANGO_SESSION (SESSION_KEY,EXPIRE_DATE) values ('qay1c8oag0dnh8b0kcmdsbl5kmzo1680',to_timestamp('12-07-22 12.30.08.633713000 AM','DD-MM-RR HH.MI.SSXFF AM'));
