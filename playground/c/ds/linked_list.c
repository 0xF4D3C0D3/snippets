#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct List {
	struct Node *head;
	struct Node *tail;

	unsigned int len;
};

struct Node {
	char *val;
	
	struct Node *next;
	struct Node *prev;
};

struct List *new_list()
{
	struct List *list = malloc(sizeof(struct List));
	list->head = list->tail = NULL;
	list->len = 0;

	return list;
}

struct Node *new_node(const char *val)
{
	struct Node *node = malloc(sizeof(struct Node));
	
	node->val = strdup(val);

	return node;
}

struct Node *find_node_at(struct List *list, unsigned int idx)
{
	if (idx > list->len)
		return list->tail;
	else if (idx < 0)
		return list->head;

	struct Node *cur = list->head;
	for (int i=0; i < idx; i++) cur = cur->next;

	return cur;
}

void insert_node(struct List *list, struct Node *node, int idx)
{
	printf("[+] insert node. node->val: %s idx: %d\n", node->val, idx);

	if (list->len == 0) {
		node->next = node;
		node->prev = node;
		list->head = list->tail = node;

		list->len++;
		return;
	}

	if (idx < 0) idx = list->len + idx + 1;

	struct Node *cur = find_node_at(list, idx);

	node->prev = cur->prev;
	node->next = cur;

	cur->prev->next = node;
	cur->prev = node;

	if (idx == 0) {
		list->head = node;
		list->tail->next = node;
	} else if (idx == list->len) {
		list->tail = node;
		list->head->prev = node;
	}

	list->len++;
}

void append_node(struct List *list, struct Node *node)
{
	printf("[+] append node. node->val: %s\n", node->val);

	insert_node(list, node, -1);
}

void prepend_node(struct List *list, struct Node *node)
{
	printf("[+] prepend node. node->val: %s\n", node->val);

	insert_node(list, node, 0);
}

void delete_node(struct List *list, int idx)
{
	printf("[+] delete node. node->val: %s idx: %d\n", list->tail->val, idx);

	if (list->len < 1) return;
	if (idx < 0) idx = list->len + idx;	// unlike insert_node, it doesn't index empty spaces
						// but elements

	struct Node *cur = find_node_at(list, idx), *tmp = cur;

	cur->prev->next = cur->next;
	cur->next->prev = cur->prev;

	if (idx == 0) {
		list->head = cur->next;
		list->tail->next = cur->next;
	} else if (idx == list->len-1) {
		list->tail = cur->prev;
		list->head->prev = cur->prev;
	}

	free(tmp->val);
	free(tmp);
	
	list->len--;
}

void pop_node(struct List *list)
{
	printf("[+] pop node. node->val: %s\n", list->tail->val);

	delete_node(list, -1);
}

void replace_node(struct List *list, struct Node *node, int idx)
{
	printf("[+] replace node. node->val: %s idx: %d\n", node->val, idx);

	delete_node(list, idx);
	insert_node(list, node, idx);
}

void free_list(struct List *list)
{
	struct Node *cur = list->head, *next;

	do {
		next = cur->next;
		free(cur->val);
		free(cur);
		cur = next;
	} while (cur != list->head);

	free(list);
}

void print_list(struct List *list)
{
	printf("[+] print list with %d elements\n\t", list->len);

	int len = 8, cur_len = 1, len_to_add;
	const int delim_len = 2;	// only delemiters length for dropping the last delimiter
	const int format_len = 4;	// quotes and delimiters length

	char *s = malloc(sizeof(char) * len);
	strcpy(s, "[");

	struct Node *cur = list->head;
	do {
		len_to_add = strlen(cur->val) + format_len;
		if (cur_len + len_to_add + 2 > len) {	// one for closing bracket, one for NULL
			len += len;
			s = realloc(s, sizeof(char) * len);
			printf("[?] s is reallocated %d -> %d\n\t", len/2, len);
		}
		sprintf(s, "%s\"%s\", ", s, cur->val);
		cur_len += len_to_add;
		cur = cur->next;
	} while (cur != list->head);

	strcpy(&s[cur_len-delim_len], "]");

	printf("%s\n", s);
	free(s);
}

void reverse_list(struct List *list)
{
	printf("[+] reverse list\n");

	struct Node *p = list->head, *q = list->tail;
	char *tmp;

	while (p != q && p->next != q) {
		tmp = p->val;
		p->val = q->val;
		q->val = tmp;

		p=p->next;
		q=q->prev;
	}
}

int main(int argc, char *argv[])
{
	struct List *list = new_list();

	append_node(list, new_node("Hello"));
	append_node(list, new_node(","));
	append_node(list, new_node("world"));
	print_list(list);

	prepend_node(list, new_node("is"));
	print_list(list);

	prepend_node(list, new_node("This"));
	print_list(list);

	reverse_list(list);
	print_list(list);

	reverse_list(list);
	print_list(list);

	pop_node(list);
	pop_node(list);
	print_list(list);

	reverse_list(list);
	print_list(list);

	insert_node(list, new_node("the"), 1);
	insert_node(list, new_node("thing"), 2);
	print_list(list);

	delete_node(list, 1);
	replace_node(list, new_node("he"), 1);
	replace_node(list, new_node("John Doe"), -1);
	print_list(list);

	char s[512];
	for (int i=1; i<=19; i++) {
		sprintf(s, "%d=%d*%d",i*i, i, i);
		append_node(list, new_node(s));	
	}
	print_list(list);

	free_list(list);
	return 0;
}
