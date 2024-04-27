#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

typedef struct NODE { //定義NODE結構
    int data;   //紀錄此節點的資料
    struct NODE* next;  //記錄指向的下個節點位址
}Node;

void add(Node* head) {   //將一筆資料插入串列的最後
    Node* current;  //建立current節點 
    current = (Node*)malloc(sizeof(Node));
    scanf("%d", &current->data);
    current->next = NULL;

    while (head->next != NULL) {    //找到串列的最後面
        head = head->next;
    }
    head->next = current;   //將current節點連在串列最後面
    printf("ADD_SUCC\n");   
}

void insert(Node* head) {   //將一筆資料插入另一筆資料之前
    int target, data;   //目標資料 要插入的資料
    scanf("%d %d", &target, &data);

    Node* current;  //建立current節點 並指向起點head
    current = (Node*)malloc(sizeof(Node));
    current = head;

    while (current != NULL) {   //以current節點向下搜尋 
        if (current->data == target) {  //直到目標節點 跳出
            break;
        }
        current = current->next;
    }
    if (current == NULL) {  //如果找到最後端還是沒找到目標 跳出
        printf("INSERT_FAIL\n");
        return;
    }

    while (head->next != current) { //從head找到目標的前一個
        head = head->next;
    }

    Node* now;  //建立now節點 代表要插入的資料
    now = (Node*)malloc(sizeof(Node));
    now->data = data;
    now->next = current;    //指向目標節點

    head->next = now;   //從目標的前一個節點 指向插入節點

    printf("INSERT_SUCC\n");
}

void del(Node* head) {  //刪除串列中的一筆資料
    int target;
    scanf("%d", &target);

    Node* current;  //建立current節點 並指向起點head
    current = (Node*)malloc(sizeof(Node));
    current = head;

    while (current != NULL) {   //以current節點向下搜尋
        if (current->data == target) {  //直到目標節點 跳出
            break;
        }
        current = current->next;
    }
    if (current == NULL) {  //如果找到最後端還是沒找到目標 跳出
        printf("DELETE_FAIL\n");
        return;
    }
    while (head->next != current) { //從head找到目標的前一個
        head = head->next;
    }

    Node* del;  //建立del節點 指向要刪除的節點
    del = (Node*)malloc(sizeof(Node));
    del = current;

    current = current->next;    //從要刪除的節點再往下
    head->next = current;      //從要刪除的節點之前 指向要刪除的節點的下一個

    free(current);  //釋放要刪除的節點的記憶體
    printf("DELETE_SUCC\n");
}

void search(Node* head) {   //尋找串列中的一筆資料
    int target;
    scanf("%d", &target);   //目標資料

    while (head!= NULL) {   //從起點找到最後端
        if (head->data == target) {   //如果找到目標資料 跳出
            printf("FOUND\n");
            break;
        }
        head = head->next;
    }
    if (head == NULL)   //如果找到最後端還是沒找到目標
        printf("NOT FOUND\n"); 
}

void update(Node* head) {   //修改串列中的一筆資料
    int target, data;
    scanf("%d %d", &target, &data); //目標資料和要改成的資料
    while (head != NULL) {  //從起點找到最後端
        if (head->data == target) { //如果有找到 修改
            head->data = data;
            printf("UPDATE_SUCC\n");
            break;
        }
        head = head->next;
    }
    if (head == NULL)   //如果找到最後端還是沒找到目標
        printf("UPDATE_FAIL\n");
}

void print(Node* head) {    //依序印出串列中的所有資料
    head = head->next;  //起始節點沒有值 要指向第一個才有值
    while (head != NULL) {  //直到最後端
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

int main() {
    Node* first;   //建立起始點
    first = (Node*)malloc(sizeof(Node));
    first->next = NULL;

    char* move; //建立判斷動作
    move = (char*)malloc(10);

    while (scanf("%s", move) != EOF) {  //輸入判斷動作
        if (strcmp("add", move) == 0)   //將一筆資料插入串列的最後
            add(first);      
        else if (strcmp("insert", move) == 0)   //將一筆資料插入另一筆資料之前
            insert(first);
        else if (strcmp("delete", move) == 0)   //刪除串列中的一筆資料
            del(first);
        else if (strcmp("search", move) == 0)   //尋找串列中的一筆資料
            search(first);
        else if (strcmp("update", move) == 0)   //修改串列中的一筆資料
            update(first);
        else if (strcmp("print", move) == 0)    //依序印出串列中的所有資料
            print(first);
    }

    free(first);    //釋放串列的記憶體
    //system("pause");
    return 0;
}