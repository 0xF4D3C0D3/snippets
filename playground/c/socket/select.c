#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 2020

int main(int argc, char *argv[])
{
	fd_set master;
	fd_set read_fds;
	struct sockaddr_in serveraddr;
	struct sockaddr_in clientaddr;
	int fdmax;
	int listener;
	int newfd;
	char buf[1024];
	int nbytes;
	int yes = 1;
	socklen_t addrlen;
	int i, j;

	FD_ZERO(&master);
	FD_ZERO(&read_fds);

	if ((listener = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
		perror("server-socket");
		exit(EXIT_FAILURE);
	}
	printf("server-socket OK\n");

	if (setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int)) == -1) {
		perror("server-sockopt");
		exit(EXIT_FAILURE);
	}
	printf("server-sockopt OK\n");

	serveraddr.sin_family = AF_INET;
	serveraddr.sin_addr.s_addr = INADDR_ANY;
	serveraddr.sin_port = htons(PORT);
	memset(&(serveraddr.sin_zero), '\0', 8);

	if (bind(listener, (struct sockaddr *)&serveraddr, sizeof(serveraddr)) == -1) {
		perror("server-bind");
		exit(EXIT_FAILURE);
	}
	printf("server-bind OK\n");

	if (listen(listener, 10) == -1) {
		perror("server-listen");
		exit(EXIT_FAILURE);
	}
	printf("server-listen OK\n");

	FD_SET(listener, &master);
	fdmax = listener;

	while(1) {
		read_fds = master;

		if (select(fdmax+1, &read_fds, NULL, NULL, NULL) == -1) {
			perror("server-select");
			exit(EXIT_FAILURE);
		}
		printf("server-select OK\n");

		for (i = 0; i <= fdmax; i++) {
			if (FD_ISSET(i, &read_fds)) {
				if (i == listener) {
					addrlen = sizeof(clientaddr);
					if ((newfd = accept(listener, (struct sockaddr *)&clientaddr, &addrlen)) == -1) {
						perror("server-accept");
					} else {
						printf("server-accept OK\n");

						FD_SET(newfd, &master);
						if (newfd > fdmax) {
							fdmax = newfd;
						}
						printf("%s: new connection from %s on socket %d\n", argv[0], inet_ntoa(clientaddr.sin_addr), newfd);
					}
				} else {
					if ((nbytes = recv(i, buf, sizeof(buf), 0)) <= 0) {
						if(nbytes == 0) {
							printf("%s: socket %d hung up\n", argv[0], i);
						} else {
							perror("recv");
						}

						close(i);
						FD_CLR(i, &master);
					} else {
						buf[nbytes-1] = '\0';
						printf("client sent \"%s\"\n", buf);
						for(j = 0; j <= fdmax; j++) {
							if (FD_ISSET(j, &master)) {
								if (j != listener && j != i) {
									if (send(j, buf, nbytes, 0) == -1) {
										perror("send");
									}
								}
							}
						}
					}
				}
			}
		}
	}

	return EXIT_SUCCESS;
}
