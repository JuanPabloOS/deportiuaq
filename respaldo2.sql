BEGIN TRANSACTION;
INSERT INTO workshop_wsmember VALUES (13,270059,'Roberto','Arteaga Solis','nuevo@gmail.com',NULL,0,8,'SOF11',70);
INSERT INTO workshop_wsmember VALUES (14,212123,'Juan Pablo','Mosqueda Hernández','nuevo@gmail.com',NULL,0,8,'SOF11',70);
INSERT INTO workshop_wsmember VALUES (15,456585,'Reyna','Olvera Sánchez','jkjbk@gmail.com',NULL,0,8,'SOF11',70);
INSERT INTO workshop_wsmember VALUES (16,789885,'Daniela','Olvera','Moreno@gmail.com',NULL,0,8,'SOF11',70);
INSERT INTO workshop_wsmember VALUES (17,252545,'Emmanuel','Olvera','kjbkj@gmail.com',NULL,0,11,'SOF11',70);
INSERT INTO workshop_wsmember VALUES (18,636363,'Antonio','Vazquez','antvagu@gmail.com',NULL,0,8,'SOF11',70,8);
INSERT INTO workshop_wsmember VALUES (19,4454545,'Roberto','Robertales','r@mail.com',NULL,0,8,'SOF11',70,8);
INSERT INTO workshop_sesion VALUES (3,'2019-10-27',8);
INSERT INTO workshop_sesion VALUES (6,'2019-10-28',8);
INSERT INTO workshop_sesion VALUES (7,'2019-10-29',11);
INSERT INTO workshop_calltherollws VALUES (11,1,13,3);
INSERT INTO workshop_calltherollws VALUES (12,1,13,3);
INSERT INTO workshop_calltherollws VALUES (13,0,14,3);
INSERT INTO workshop_calltherollws VALUES (14,1,14,6);
INSERT INTO workshop_calltherollws VALUES (15,0,15,3);
INSERT INTO workshop_calltherollws VALUES (16,0,15,6);
INSERT INTO workshop_calltherollws VALUES (17,1,16,3);
INSERT INTO workshop_calltherollws VALUES (18,0,16,6);
INSERT INTO workshop_calltherollws VALUES (19,1,17,7);
INSERT INTO workshop_workshop VALUES (8,'Varonil','Futbol','Lunes y Miércoles 13:00 - 15:00 hrs',NULL,'2019-2',10,8,10);
INSERT INTO workshop_workshop VALUES (11,'Varonil','Basketball','Miécoles - Viernes 12:00 - 14:00',NULL,'2019-2',10,8,1);
INSERT INTO workshop_workshop VALUES (12,'Femenil','Atletismo','Lunes y Miércoles 13:00 - 15:00 hrs',NULL,'2019-2',NULL,8,0);
INSERT INTO core_user VALUES (1,'pbkdf2_sha256$150000$bxvRg92f9tMN$nNPANNOJZr2tw0vH9UYiWCCAtg+PNFXnud9uB/taTrg=','2019-10-26 17:38:54.616057',1,'juan','Juan Pablo','Olvera Sánchez','jp.oes@hotmail.com',1,1,'2019-09-19 19:21:33','AD');
INSERT INTO core_user VALUES (2,'pbkdf2_sha256$150000$3gFdXbxzTrvm$5AuAjSEYMcU8G3ZCYXKQBMZuomP8XlDWmo2dgP84GUU=','2019-09-25 02:00:32.051170',0,'Roberto','Roberto','Arteaga Solis','roberto@gmail.com',0,1,'2019-09-23 13:10:01.523682','DC');
INSERT INTO core_user VALUES (3,'pbkdf2_sha256$150000$ArB3TUXw5M9C$OThpVX9SiKxItG9TGCrcpnb1WIZc7Jy1FtayojNFGnw=',NULL,0,'Roberto2','Roberto','Arteaga Solís','roberto@gmail.com',0,1,'2019-09-24 02:07:55.361050','BC');
INSERT INTO core_user VALUES (4,'pbkdf2_sha256$150000$iSwJa4TFNsUq$lwTqTw63UvQ/Bh0YralOczhfsiiP8ifH8lOuZT/nuYQ=',NULL,0,'Superjuan','Juan Pablo','Olvera','jp.oes@gmail.com',0,1,'2019-09-24 02:14:34.290841','AD');
INSERT INTO core_user VALUES (5,'pbkdf2_sha256$150000$o5p4QtWgxPA7$NkjonTkbtq2ErkDhtES/C1UKdGLRHuLR2FGgKFWlBaA=',NULL,0,'ricardo','Ricardo','Sánchez','ric@gmail.com',0,0,'2019-10-01 22:08:03','AD');
INSERT INTO core_user VALUES (6,'pbkdf2_sha256$150000$MitSxjqAuOxc$VjFXxENXBa0ouEdswBPKOCN2AHIck0K5sTRHdiKsBuU=',NULL,0,'Alex','Alejandro','Vargas','lex.vargas@gmail.com',0,0,'2019-10-01 22:21:42.603500','DC');
INSERT INTO core_user VALUES (7,'pbkdf2_sha256$150000$FUvFIEjKS9pu$HQDnWLJUL0fz9V8K0VlvaSxA5ma2AysCxhUJHY99p3w=','2019-10-11 18:20:52.562190',0,'Haziel','Haziel','Sánchez Sánchez','ricsan@gmail.com',0,1,'2019-10-11 18:17:00.465807','DC');
INSERT INTO core_user VALUES (8,'pbkdf2_sha256$150000$wpX69hh9VP07$8M/5nRWk0DW079n5ammmvtH8J57j+nq1YkU3btiMVoc=','2019-10-29 18:20:29.568998',0,'docente','docente','docente','docente@gmail.com',0,1,'2019-10-14 19:56:29.454851','DC');
INSERT INTO django_session VALUES ('8vz1pesck4q33pnqxky7y0ao9nq8qudi','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-20 12:27:50.245314');
INSERT INTO django_session VALUES ('7pex5h70y72rd0zcor6om4wihdk1isqg','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-23 07:14:53.667427');
INSERT INTO django_session VALUES ('2ty8uqsyto7o0utedug7eimoc32r4m8v','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-23 07:20:31.548223');
INSERT INTO django_session VALUES ('61x0j9a9ofthjelgw142lfaom700n385','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-23 07:22:18.952488');
INSERT INTO django_session VALUES ('wxy6d1mprpr8exbpfllm6nox8lkxh0jg','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-23 07:22:48.624974');
INSERT INTO django_session VALUES ('pxc80g9bcmc20jj14f5e9zsq51sv2mmj','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-23 07:27:59.532584');
INSERT INTO django_session VALUES ('p1uwhostg45ruk6kqhlyapq4s6zps9v2','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-23 07:30:05.009856');
INSERT INTO django_session VALUES ('i0dfxt874bzjn084ebawe2q84trp1tzo','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-23 07:32:24.817238');
INSERT INTO django_session VALUES ('1yepcuuzkq1bs9u02lq0b17n2911s5cp','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-23 07:42:19.400334');
INSERT INTO django_session VALUES ('ruyw6kdvg489u2eeel4ydcrcfugxk06d','ZGU3ZTBkMjZkNWJiNTQyYTM5ZDcxNjg1MTYxNTZmZjQ3ZWFlMmI0NTp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDB9','2019-09-23 07:45:38.524932');
INSERT INTO django_session VALUES ('t63auhhjl9zjwjjwetjxd90tbezcfx72','MjczNjZlNzA3N2M3Zjc0YTFlZDQyNzJhNGNlODNlZmJjZjlkYmI2Mzp7fQ==','2019-10-06 21:50:43.888059');
INSERT INTO django_session VALUES ('aik6zgr998o3xu1gff3yreb3u9nafffn','MjM1M2FlMGY4NWFhYTEwZTM1NThhM2E3ODBhMmQ4OTBmZDQzOTIwMDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMTUxZTgwYWE2YjAyYzQ1YThhNTU5OWVmN2Y0NDMwM2Y3NDRmNjc4In0=','2019-09-23 09:25:31.273084');
INSERT INTO django_session VALUES ('v0zgn55wli087diyq4fv4326k69ut01h','YjQ3M2QwYWQ3ZTE1OGRiZWVkNTVjYTYxMzkyZjFkNzI2ODExM2VkNDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NjAwODJhNGEyN2Y3NWJkMTEyMGEwOTJmYmUwYjIwODU4YmFjMGNlIn0=','2019-09-23 23:15:34.553159');
INSERT INTO django_session VALUES ('9abouyfpzuzo1xjiitqirc6b1gkoggdx','MjM1M2FlMGY4NWFhYTEwZTM1NThhM2E3ODBhMmQ4OTBmZDQzOTIwMDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMTUxZTgwYWE2YjAyYzQ1YThhNTU5OWVmN2Y0NDMwM2Y3NDRmNjc4In0=','2019-10-02 08:07:04.154412');
INSERT INTO django_session VALUES ('ivyh7gv5fzhr6bj2zdjivhtzzeg1g1xb','MjM1M2FlMGY4NWFhYTEwZTM1NThhM2E3ODBhMmQ4OTBmZDQzOTIwMDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMTUxZTgwYWE2YjAyYzQ1YThhNTU5OWVmN2Y0NDMwM2Y3NDRmNjc4In0=','2019-10-08 05:49:02.195160');
INSERT INTO django_session VALUES ('kgagpfkxller9k3a0fiku145ifj2sqh1','MmRlMDdmYjkwNGFjMmI3OTAzODJjMTU2OWE3ZGMxN2RlNzU0NmFiZjp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5NzIzNDY2ZmUyY2JlNjI5YTJmZTFjYjAzZDQ2NWE4ODNkNWFkNDU2In0=','2019-10-12 04:20:52.691228');
INSERT INTO django_session VALUES ('0qx9sqhd0fr45ex80ejcgp8dovx4r5oj','MjM1M2FlMGY4NWFhYTEwZTM1NThhM2E3ODBhMmQ4OTBmZDQzOTIwMDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMTUxZTgwYWE2YjAyYzQ1YThhNTU5OWVmN2Y0NDMwM2Y3NDRmNjc4In0=','2019-10-13 12:27:48.969605');
INSERT INTO django_session VALUES ('naacr9h1xppvsxx6v6xc8t0owjctdtxj','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-15 06:29:32.865111');
INSERT INTO django_session VALUES ('kh684euvj76jenh5au7qg13x2rhocb2w','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-16 02:59:57.876183');
INSERT INTO django_session VALUES ('ialh35yvvjnef3kj8e5btzriqkjw2mkz','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-17 05:59:58.497921');
INSERT INTO django_session VALUES ('vpk2549bgci5w9rqjm24djgdrz33besn','MjM1M2FlMGY4NWFhYTEwZTM1NThhM2E3ODBhMmQ4OTBmZDQzOTIwMDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMTUxZTgwYWE2YjAyYzQ1YThhNTU5OWVmN2Y0NDMwM2Y3NDRmNjc4In0=','2019-10-18 07:18:37.887470');
INSERT INTO django_session VALUES ('2mvm0atfvgpqgtzltut5cwlwifss4hc6','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-18 08:15:42.907566');
INSERT INTO django_session VALUES ('cea8jo8yr3i4ii5zerqq8zgykpf7147b','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-19 02:47:46.230190');
INSERT INTO django_session VALUES ('ahurc89uxuuxckbcoa6wbvrzyz67f0ju','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-22 07:02:43.029533');
INSERT INTO django_session VALUES ('5616zfu4c29y6tczme2q4913691icu58','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-23 06:30:54.531017');
INSERT INTO django_session VALUES ('icwylnufkoz7gnoe3xy5m3e6trtui6t2','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-27 03:10:09.825311');
INSERT INTO django_session VALUES ('y1403pqp1i6x2tbju9rcs1k1ehnuvhqp','NjY2NWQ0NjRiY2VlOGZjMWZjZjE1OTE2NWM3Y2NiNDNiYTcxZWIyOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMTUxZTgwYWE2YjAyYzQ1YThhNTU5OWVmN2Y0NDMwM2Y3NDRmNjc4In0=','2019-11-09 17:38:55.035896');
INSERT INTO django_session VALUES ('ouon9o02in733c6402zym4ahwg0egfs1','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-28 07:38:44.915420');
INSERT INTO django_session VALUES ('4kt0eehkxj2vosspjfaln04ext94xo8o','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-29 08:01:54.807238');
INSERT INTO django_session VALUES ('d1gi57j03gla5gua4qdzxtm5vlfrmkt6','YTMzNWVmODljYTkzZjMzM2M3ZWRhY2U1MzRiYzA3ODVmYzVmZGY3MDp7Il9zZXNzaW9uX2V4cGlyeSI6MzYwMDAsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjNjg3OWE3YzMwYjZiOTkzOTAzMmM2MjY3NmUzY2JhOTA0NjMxNTEwIn0=','2019-10-30 04:20:29.852461');
INSERT INTO django_admin_log VALUES (1,'2019-09-22 23:25:02.163728','1','juan','[{changed: {fields: [first_name, last_name, email]}}]',6,1,2);
INSERT INTO django_admin_log VALUES (2,'2019-09-30 19:55:19.938436','1','Workshop object (1)','[{added: {}}]',9,1,1);
INSERT INTO django_admin_log VALUES (3,'2019-10-01 20:33:45.479780','2','Futbol Varonil','[{changed: {fields: [branch, sport]}}]',9,1,2);
INSERT INTO django_admin_log VALUES (4,'2019-10-01 20:33:54.510792','1','Futbol Femenil','[{changed: {fields: [branch, sport]}}]',9,1,2);
INSERT INTO django_admin_log VALUES (5,'2019-10-01 22:14:33.138564','5','Ricardo Sánchez','[{changed: {fields: [userType]}}]',6,1,2);
INSERT INTO django_admin_log VALUES (6,'2019-10-14 20:29:18.336825','2','Futbol Femenil','[{changed: {fields: [schedule]}}]',17,1,2);
INSERT INTO django_admin_log VALUES (7,'2019-10-14 20:30:55.027853','1','Futbol Varonil','[{changed: {fields: [schedule]}}]',17,1,2);
INSERT INTO django_admin_log VALUES (8,'2019-10-15 17:41:16.155869','4','Basketball Femenil','[{changed: {fields: [responsible]}}]',17,1,2);
INSERT INTO django_admin_log VALUES (9,'2019-10-15 17:41:25.358503','3','Futbol Varonil','[{changed: {fields: [responsible]}}]',17,1,2);
INSERT INTO django_admin_log VALUES (10,'2019-10-15 17:41:33.442348','2','Futbol Femenil','[{changed: {fields: [responsible]}}]',17,1,2);
INSERT INTO django_admin_log VALUES (11,'2019-10-15 17:41:41.022796','1','Futbol Varonil','[{changed: {fields: [responsible]}}]',17,1,2);
INSERT INTO django_admin_log VALUES (12,'2019-10-16 01:27:36.120621','2','WsMember object (2)','',15,1,3);
INSERT INTO django_admin_log VALUES (13,'2019-10-16 20:19:44.248968','1','WsMember object (1)','',15,1,3);
INSERT INTO django_admin_log VALUES (14,'2019-10-27 22:10:22.391111','1','Sesion object (1)','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (15,'2019-10-27 22:13:49.160666','1','CallTheRollWs object (1)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (16,'2019-10-27 22:13:58.961889','2','CallTheRollWs object (2)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (17,'2019-10-27 22:14:08.033801','3','CallTheRollWs object (3)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (18,'2019-10-27 23:32:21.668470','3','Futbol Varonil','',17,1,3);
INSERT INTO django_admin_log VALUES (19,'2019-10-27 23:32:46.184079','10','olvera ema','',15,1,3);
INSERT INTO django_admin_log VALUES (20,'2019-10-27 23:32:47.290130','9','Moreno Reyna','',15,1,3);
INSERT INTO django_admin_log VALUES (21,'2019-10-27 23:32:47.451003','8','Arteaga Solís dd','',15,1,3);
INSERT INTO django_admin_log VALUES (22,'2019-10-27 23:32:47.626354','7','nuevo nuevo','',15,1,3);
INSERT INTO django_admin_log VALUES (23,'2019-10-27 23:32:47.753016','6','Mosqueda Hernández Juan Pablo','',15,1,3);
INSERT INTO django_admin_log VALUES (24,'2019-10-27 23:32:47.880676','5','Mosqueda Hernández Juan Pablo','',15,1,3);
INSERT INTO django_admin_log VALUES (25,'2019-10-27 23:32:48.006669','4','Arteaga Solis Roberto','',15,1,3);
INSERT INTO django_admin_log VALUES (26,'2019-10-27 23:35:21.484006','1','Futbol Varonil','',17,1,3);
INSERT INTO django_admin_log VALUES (27,'2019-10-27 23:35:37.118654','7','eSports Varonil','',17,1,3);
INSERT INTO django_admin_log VALUES (28,'2019-10-27 23:35:37.328068','6','Tiro con arco Varonil','',17,1,3);
INSERT INTO django_admin_log VALUES (29,'2019-10-27 23:35:37.444242','5','Tiro con arco Femenil','',17,1,3);
INSERT INTO django_admin_log VALUES (30,'2019-10-27 23:35:37.592846','4','Basketball Femenil','',17,1,3);
INSERT INTO django_admin_log VALUES (31,'2019-10-27 23:35:37.708536','2','Futbol Femenil','',17,1,3);
INSERT INTO django_admin_log VALUES (32,'2019-10-28 00:47:14.253899','2','Futbol Varonil 2019-10-27','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (33,'2019-10-28 00:47:22.103456','3','Futbol Varonil 2019-10-27','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (34,'2019-10-28 00:47:31.944092','4','Tochito Varonil 2019-10-27','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (35,'2019-10-28 00:48:32.377108','4','CallTheRollWs object (4)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (36,'2019-10-28 00:48:44.373091','5','CallTheRollWs object (5)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (37,'2019-10-28 00:49:00.115028','6','CallTheRollWs object (6)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (38,'2019-10-28 01:44:07.327654','4','CallTheRollWs object (4)','',16,1,3);
INSERT INTO django_admin_log VALUES (39,'2019-10-28 01:46:25.308340','8','Futbol Varonil','[{changed: {fields: [maxMembers]}}]',17,1,2);
INSERT INTO django_admin_log VALUES (40,'2019-10-28 01:47:51.510420','7','CallTheRollWs object (7)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (41,'2019-10-28 01:50:51.348407','8','CallTheRollWs object (8)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (42,'2019-10-28 01:51:07.323775','9','CallTheRollWs object (9)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (43,'2019-10-28 01:51:31.844919','10','CallTheRollWs object (10)','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (44,'2019-10-28 21:43:28.909370','11','Moreno Juan Pablo','',15,1,3);
INSERT INTO django_admin_log VALUES (45,'2019-10-28 21:44:30.335253','5','Tochito Varonil 2019-10-28','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (46,'2019-10-28 21:44:37.508011','6','Tochito Varonil 2019-10-28','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (47,'2019-10-28 21:45:01.694108','6','Tochito Varonil 2019-10-28','',23,1,3);
INSERT INTO django_admin_log VALUES (48,'2019-10-28 21:51:26.711418','None','Tochito Varonil 2019-10-28','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (49,'2019-10-28 21:51:38.312246','None','Tochito Varonil 2019-10-28','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (50,'2019-10-28 21:52:58.516785','10','Tochito Varonil','',17,1,3);
INSERT INTO django_admin_log VALUES (51,'2019-10-28 21:52:58.752402','9','Basketball Varonil','',17,1,3);
INSERT INTO django_admin_log VALUES (52,'2019-10-28 21:57:04.347360','2','Futbol Varonil 2019-10-27','',23,1,3);
INSERT INTO django_admin_log VALUES (53,'2019-10-28 21:57:22.700891','6','Futbol Varonil 2019-10-28','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (54,'2019-10-28 21:58:57.439124','11','True Arteaga Solis Roberto','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (55,'2019-10-28 21:59:03.899200','12','True Arteaga Solis Roberto','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (56,'2019-10-28 21:59:13.305970','13','False Mosqueda Hernández Juan Pablo','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (57,'2019-10-28 21:59:21.989166','14','True Mosqueda Hernández Juan Pablo','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (58,'2019-10-28 21:59:30.884136','15','False Olvera Sánchez Reyna','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (59,'2019-10-28 22:00:03.658413','16','False Olvera Sánchez Reyna','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (60,'2019-10-28 22:00:11.457731','17','True Olvera Daniela','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (61,'2019-10-28 22:00:19.545907','18','False Olvera Daniela','[{added: {}}]',16,1,1);
INSERT INTO django_admin_log VALUES (62,'2019-10-29 02:55:43.310007','11','Basketball Varonil','[{added: {}}]',17,1,1);
INSERT INTO django_admin_log VALUES (63,'2019-10-29 02:56:47.962216','7','Basketball Varonil 2019-10-29','[{added: {}}]',23,1,1);
INSERT INTO django_admin_log VALUES (64,'2019-10-29 02:57:13.705349','19','True Olvera Emmanuel','[{added: {}}]',16,1,1);
INSERT INTO auth_permission VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES (5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES (6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES (8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES (9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES (10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES (11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES (12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES (13,4,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES (14,4,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES (15,4,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES (16,4,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES (17,5,'add_session','Can add session');
INSERT INTO auth_permission VALUES (18,5,'change_session','Can change session');
INSERT INTO auth_permission VALUES (19,5,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES (20,5,'view_session','Can view session');
INSERT INTO auth_permission VALUES (21,6,'add_user','Can add user');
INSERT INTO auth_permission VALUES (22,6,'change_user','Can change user');
INSERT INTO auth_permission VALUES (23,6,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES (24,6,'view_user','Can view user');
INSERT INTO auth_permission VALUES (25,7,'add_match','Can add match');
INSERT INTO auth_permission VALUES (26,7,'change_match','Can change match');
INSERT INTO auth_permission VALUES (27,7,'delete_match','Can delete match');
INSERT INTO auth_permission VALUES (28,7,'view_match','Can view match');
INSERT INTO auth_permission VALUES (29,8,'add_team','Can add team');
INSERT INTO auth_permission VALUES (30,8,'change_team','Can change team');
INSERT INTO auth_permission VALUES (31,8,'delete_team','Can delete team');
INSERT INTO auth_permission VALUES (32,8,'view_team','Can view team');
INSERT INTO auth_permission VALUES (33,9,'add_workshop','Can add workshop');
INSERT INTO auth_permission VALUES (34,9,'change_workshop','Can change workshop');
INSERT INTO auth_permission VALUES (35,9,'delete_workshop','Can delete workshop');
INSERT INTO auth_permission VALUES (36,9,'view_workshop','Can view workshop');
INSERT INTO auth_permission VALUES (37,10,'add_wsmember','Can add ws member');
INSERT INTO auth_permission VALUES (38,10,'change_wsmember','Can change ws member');
INSERT INTO auth_permission VALUES (39,10,'delete_wsmember','Can delete ws member');
INSERT INTO auth_permission VALUES (40,10,'view_wsmember','Can view ws member');
INSERT INTO auth_permission VALUES (41,11,'add_teammember','Can add team member');
INSERT INTO auth_permission VALUES (42,11,'change_teammember','Can change team member');
INSERT INTO auth_permission VALUES (43,11,'delete_teammember','Can delete team member');
INSERT INTO auth_permission VALUES (44,11,'view_teammember','Can view team member');
INSERT INTO auth_permission VALUES (45,12,'add_player','Can add player');
INSERT INTO auth_permission VALUES (46,12,'change_player','Can change player');
INSERT INTO auth_permission VALUES (47,12,'delete_player','Can delete player');
INSERT INTO auth_permission VALUES (48,12,'view_player','Can view player');
INSERT INTO auth_permission VALUES (49,13,'add_calltherollteam','Can add call the roll team');
INSERT INTO auth_permission VALUES (50,13,'change_calltherollteam','Can change call the roll team');
INSERT INTO auth_permission VALUES (51,13,'delete_calltherollteam','Can delete call the roll team');
INSERT INTO auth_permission VALUES (52,13,'view_calltherollteam','Can view call the roll team');
INSERT INTO auth_permission VALUES (53,14,'add_calltherollws','Can add call the roll ws');
INSERT INTO auth_permission VALUES (54,14,'change_calltherollws','Can change call the roll ws');
INSERT INTO auth_permission VALUES (55,14,'delete_calltherollws','Can delete call the roll ws');
INSERT INTO auth_permission VALUES (56,14,'view_calltherollws','Can view call the roll ws');
INSERT INTO auth_permission VALUES (57,15,'add_wsmember','Can add Miembro de taller');
INSERT INTO auth_permission VALUES (58,15,'change_wsmember','Can change Miembro de taller');
INSERT INTO auth_permission VALUES (59,15,'delete_wsmember','Can delete Miembro de taller');
INSERT INTO auth_permission VALUES (60,15,'view_wsmember','Can view Miembro de taller');
INSERT INTO auth_permission VALUES (61,16,'add_calltherollws','Can add call the roll ws');
INSERT INTO auth_permission VALUES (62,16,'change_calltherollws','Can change call the roll ws');
INSERT INTO auth_permission VALUES (63,16,'delete_calltherollws','Can delete call the roll ws');
INSERT INTO auth_permission VALUES (64,16,'view_calltherollws','Can view call the roll ws');
INSERT INTO auth_permission VALUES (65,17,'add_workshop','Can add Taller deportivo');
INSERT INTO auth_permission VALUES (66,17,'change_workshop','Can change Taller deportivo');
INSERT INTO auth_permission VALUES (67,17,'delete_workshop','Can delete Taller deportivo');
INSERT INTO auth_permission VALUES (68,17,'view_workshop','Can view Taller deportivo');
INSERT INTO auth_permission VALUES (69,18,'add_calltherollteam','Can add call the roll team');
INSERT INTO auth_permission VALUES (70,18,'change_calltherollteam','Can change call the roll team');
INSERT INTO auth_permission VALUES (71,18,'delete_calltherollteam','Can delete call the roll team');
INSERT INTO auth_permission VALUES (72,18,'view_calltherollteam','Can view call the roll team');
INSERT INTO auth_permission VALUES (73,19,'add_teammember','Can add Miembro de equipo');
INSERT INTO auth_permission VALUES (74,19,'change_teammember','Can change Miembro de equipo');
INSERT INTO auth_permission VALUES (75,19,'delete_teammember','Can delete Miembro de equipo');
INSERT INTO auth_permission VALUES (76,19,'view_teammember','Can view Miembro de equipo');
INSERT INTO auth_permission VALUES (77,20,'add_match','Can add Partido');
INSERT INTO auth_permission VALUES (78,20,'change_match','Can change Partido');
INSERT INTO auth_permission VALUES (79,20,'delete_match','Can delete Partido');
INSERT INTO auth_permission VALUES (80,20,'view_match','Can view Partido');
INSERT INTO auth_permission VALUES (81,21,'add_team','Can add Equipo Representativo');
INSERT INTO auth_permission VALUES (82,21,'change_team','Can change Equipo Representativo');
INSERT INTO auth_permission VALUES (83,21,'delete_team','Can delete Equipo Representativo');
INSERT INTO auth_permission VALUES (84,21,'view_team','Can view Equipo Representativo');
INSERT INTO auth_permission VALUES (85,22,'add_player','Can add Jugador');
INSERT INTO auth_permission VALUES (86,22,'change_player','Can change Jugador');
INSERT INTO auth_permission VALUES (87,22,'delete_player','Can delete Jugador');
INSERT INTO auth_permission VALUES (88,22,'view_player','Can view Jugador');
INSERT INTO auth_permission VALUES (89,23,'add_sesion','Can add sesion');
INSERT INTO auth_permission VALUES (90,23,'change_sesion','Can change sesion');
INSERT INTO auth_permission VALUES (91,23,'delete_sesion','Can delete sesion');
INSERT INTO auth_permission VALUES (92,23,'view_sesion','Can view sesion');
INSERT INTO django_content_type VALUES (1,'admin','logentry');
INSERT INTO django_content_type VALUES (2,'auth','permission');
INSERT INTO django_content_type VALUES (3,'auth','group');
INSERT INTO django_content_type VALUES (4,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES (5,'sessions','session');
INSERT INTO django_content_type VALUES (6,'core','user');
INSERT INTO django_content_type VALUES (7,'core','match');
INSERT INTO django_content_type VALUES (8,'core','team');
INSERT INTO django_content_type VALUES (9,'core','workshop');
INSERT INTO django_content_type VALUES (10,'core','wsmember');
INSERT INTO django_content_type VALUES (11,'core','teammember');
INSERT INTO django_content_type VALUES (12,'core','player');
INSERT INTO django_content_type VALUES (13,'core','calltherollteam');
INSERT INTO django_content_type VALUES (14,'core','calltherollws');
INSERT INTO django_content_type VALUES (15,'workshop','wsmember');
INSERT INTO django_content_type VALUES (16,'workshop','calltherollws');
INSERT INTO django_content_type VALUES (17,'workshop','workshop');
INSERT INTO django_content_type VALUES (18,'team','calltherollteam');
INSERT INTO django_content_type VALUES (19,'team','teammember');
INSERT INTO django_content_type VALUES (20,'team','match');
INSERT INTO django_content_type VALUES (21,'team','team');
INSERT INTO django_content_type VALUES (22,'team','player');
INSERT INTO django_content_type VALUES (23,'workshop','sesion');
INSERT INTO django_migrations VALUES (1,'contenttypes','0001_initial','2019-09-17 22:54:48.499860');
INSERT INTO django_migrations VALUES (2,'contenttypes','0002_remove_content_type_name','2019-09-17 22:54:48.696405');
INSERT INTO django_migrations VALUES (3,'auth','0001_initial','2019-09-17 22:54:48.862960');
INSERT INTO django_migrations VALUES (4,'auth','0002_alter_permission_name_max_length','2019-09-17 22:54:49.068828');
INSERT INTO django_migrations VALUES (5,'auth','0003_alter_user_email_max_length','2019-09-17 22:54:49.201162');
INSERT INTO django_migrations VALUES (6,'auth','0004_alter_user_username_opts','2019-09-17 22:54:49.341259');
INSERT INTO django_migrations VALUES (7,'auth','0005_alter_user_last_login_null','2019-09-17 22:54:49.499049');
INSERT INTO django_migrations VALUES (8,'auth','0006_require_contenttypes_0002','2019-09-17 22:54:49.622163');
INSERT INTO django_migrations VALUES (9,'auth','0007_alter_validators_add_error_messages','2019-09-17 22:54:49.768343');
INSERT INTO django_migrations VALUES (10,'auth','0008_alter_user_username_max_length','2019-09-17 22:54:50.802961');
INSERT INTO django_migrations VALUES (11,'auth','0009_alter_user_last_name_max_length','2019-09-17 22:54:51.207858');
INSERT INTO django_migrations VALUES (12,'auth','0010_alter_group_name_max_length','2019-09-17 22:54:51.540556');
INSERT INTO django_migrations VALUES (13,'auth','0011_update_proxy_permissions','2019-09-17 22:54:51.775432');
INSERT INTO django_migrations VALUES (14,'core','0001_initial','2019-09-17 22:54:52.043593');
INSERT INTO django_migrations VALUES (15,'admin','0001_initial','2019-09-17 22:54:52.574033');
INSERT INTO django_migrations VALUES (16,'admin','0002_logentry_remove_auto_add','2019-09-17 22:54:53.273334');
INSERT INTO django_migrations VALUES (17,'admin','0003_logentry_add_action_flag_choices','2019-09-17 22:54:54.120260');
INSERT INTO django_migrations VALUES (18,'sessions','0001_initial','2019-09-17 22:54:54.483848');
INSERT INTO django_migrations VALUES (19,'core','0002_auto_20190926_1749','2019-09-26 23:06:39.378415');
INSERT INTO django_migrations VALUES (20,'core','0003_auto_20191001_1109','2019-10-01 16:09:49.242851');
INSERT INTO django_migrations VALUES (21,'core','0004_auto_20191001_1529','2019-10-01 20:29:54.475597');
INSERT INTO django_migrations VALUES (22,'core','0005_auto_20191001_1552','2019-10-01 20:52:20.427232');
INSERT INTO django_migrations VALUES (23,'core','0006_wsmember_expediente','2019-10-07 20:13:46.896054');
INSERT INTO django_migrations VALUES (24,'core','0007_auto_20191007_1513','2019-10-07 20:13:47.234668');
INSERT INTO django_migrations VALUES (25,'core','0008_auto_20191013_1800','2019-10-13 23:00:49.916760');
INSERT INTO django_migrations VALUES (26,'team','0001_initial','2019-10-13 23:00:50.187949');
INSERT INTO django_migrations VALUES (27,'workshop','0001_initial','2019-10-13 23:00:50.415002');
INSERT INTO django_migrations VALUES (28,'workshop','0002_auto_20191016_1556','2019-10-16 20:56:40.462541');
INSERT INTO django_migrations VALUES (29,'team','0002_auto_20191023_1530','2019-10-23 20:30:14.137660');
INSERT INTO django_migrations VALUES (30,'workshop','0003_remove_calltherollws_idws','2019-10-23 20:30:14.417050');
INSERT INTO django_migrations VALUES (31,'workshop','0004_wsmember_plan','2019-10-26 17:17:40.864287');
INSERT INTO django_migrations VALUES (32,'workshop','0005_wsmember_group','2019-10-26 17:38:05.297191');
INSERT INTO django_migrations VALUES (33,'workshop','0006_auto_20191027_1536','2019-10-27 21:37:05.341476');
INSERT INTO django_migrations VALUES (34,'workshop','0007_auto_20191028_1550','2019-10-28 21:51:04.073882');
INSERT INTO django_migrations VALUES (35,'workshop','0008_auto_20191029_1555','2019-10-29 21:55:31.452220');
COMMIT;
