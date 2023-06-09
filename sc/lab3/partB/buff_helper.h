#ifndef CIRC_BUFF
#define CIRC_BUFF

typedef struct {
    char * const buffer;
    const int maxlen;
    int head;
    int tail;
} circ_buff_t;

int circ_buff_push(circ_buff_t *c, char data)
{
    int next;

    next = c->head + 1;  // next is where head will point to after this write.
    if (next >= c->maxlen)
        next = 0;

    if (next == c->tail)  // if the head + 1 == tail, circular buffer is full
        return -1;

    c->buffer[c->head] = data;  // Load data and then move
    c->head = next;             // head to next data offset.
    return 0;  // return success to indicate successful push.
}

int circ_buff_pop(circ_buff_t *c, char *ret_data)
{
    int next;

    if (c->head == c->tail)  // if the head == tail, we don't have any data
        return -1;

    next = c->tail + 1;  // next is where tail will point to after this read.
    if(next >= c->maxlen)
        next = 0;

    *ret_data = c->buffer[c->tail];  // Read data and then move
    c->tail = next;              // tail to next offset.
    return 0;  // return success to indicate successful push.
}

unsigned char circ_buff_isfull(circ_buff_t *c)
{   
    return ( ((c->head + 1)%c->maxlen) == c->tail);
}

unsigned char circ_buff_isempty(circ_buff_t *c)
{
    return (c->head == c->tail);
}


#endif