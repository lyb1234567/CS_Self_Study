#include "leptjson.h"
#include <errno.h>
#include <math.h> 
#include <assert.h>  /* assert() */
#include <stdlib.h>  /* NULL */
#include <string.h>
#define EXPECT(c, ch)       do { assert(*c->json == (ch)); c->json++; } while(0)
//判断该字符是否为0-9或者1-9的字符
#define ISDIGIT0TO9(ch)((ch)>='0' && (ch)<='9')
#define ISDIGIT1TO9(ch)((ch)>='1' && (ch)<='9')
typedef struct {
    const char* json;
}lept_context;

//解析是否含有空白字符
static void lept_parse_whitespace(lept_context* c) {
    const char* p = c->json;
    while (*p == ' ' || *p == '\t' || *p == '\r' || *p == '\n')
    {
        p = p + 1;
    }
    
}

//解析传入的文本是否是 “null”,如果传入的json文本不是“null”，则返回LEPT_PARSE_INVALID_VALUE。
//如果是，那么该json的数据类型就是null,然后返回LEPT_PARSE_OK,表示解析成功

static int lept_parse_iteral(lept_context* c, lept_value* v)
{
    if (*c->json == 'n')
    {
        c->json = c->json + 1;
        if (c->json[0] == 'u' && c->json[1] == 'l' && c->json[2] == 'l')
        {
                c->json = c->json + 3;
                v->type = LEPT_NULL;
                return LEPT_PARSE_OK;
        }
        else
        {
            return LEPT_PARSE_INVALID_VALUE;
        }
    }
    if (*c->json == 'f')
    {
        c->json = c->json + 1;
        if (c->json[0] == 'a' && c->json[1] == 'l' && c->json[2] == 's'&& c->json[3] == 'e')
        {
            c->json = c->json + 4;
            v->type = LEPT_FALSE;
            return LEPT_PARSE_OK;
        }
        else
        {
            return LEPT_PARSE_INVALID_VALUE;
        }
    }
    if (*c->json == 't')
    {
        c->json = c->json + 1;
        if (c->json[0] == 'r' && c->json[1] == 'u' && c->json[2] == 'e' )
        {
                c->json = c->json + 3;
                v->type = LEPT_TRUE;
                return LEPT_PARSE_OK;
        }
        else
        {
            return LEPT_PARSE_INVALID_VALUE;
        }
    }  
}

static int lept_parse_number(lept_context* c, lept_value* v)
{
    const char* p = c->json;
    if (*p == '-') p++;
    if (*p == '0')
    {
        p++;
        if (ISDIGIT1TO9(*p))
        {
            return LEPT_PARSE_INVALID_VALUE;
        }
    }
    else {
        if (!ISDIGIT1TO9(*p)) return LEPT_PARSE_INVALID_VALUE;
        for (p++; ISDIGIT0TO9(*p); p++);
    }
    //假如是整数，那么以下代码就不用看了，否则有几个字符需要检查一下
    if (*p == '.')
    {
        //检测到小数点，那么就看看下一位是否是数字,如果不是，那么就返回LEPT_PARSE_INVALID_VALUE，不然就继续遍历
        p++;
        if (!ISDIGIT0TO9(*p))
        {
            return LEPT_PARSE_INVALID_VALUE;
        }
        for (p++; ISDIGIT0TO9(*p); p++);
    }
    //如果小数点后续遍历完（或者不需要遍历），就开始判断是否是科学计数法
    if (*p == 'E' || *p == 'e')
    {
        //如果检测到是10位的科学计数法,就遍历后一位，看看是否是'+'还是'-'号,如果是就继续遍历，如果不是，那么就返回错误码
        p++;
        if (*p == '+' || *p == '-') p++;
        if (!ISDIGIT0TO9(*p))
        {
            return LEPT_PARSE_INVALID_VALUE;
        }
        //然后就继续遍历
        for (p++; ISDIGIT0TO9(*p); p++);
    }
    //程序刚刚启动的时候，errno 被设置为 0；
    //程序在运行过程中，任何一个函数发生错误都有可能修改 errno 的值，让其变为一个非零值，用以告知用户发生了特定类型的错误,我们先设置该变量为0
    //如果后续有函数出错，那么该变量就会发生变化。
    errno = 0;
    v->n = strtod(c->json, NULL);
    //检测数据大小，如果大于一个特定值或者小于一个特定值
    if (errno == ERANGE && (v->n == HUGE_VAL || v->n == -HUGE_VAL))
        return LEPT_PARSE_NUMBER_TOO_BIG;
    v->type = LEPT_NUMBER;
    c->json = p;
    return LEPT_PARSE_OK;
}

//1.解析传入的json文本，如果开头是n,那么判断是否是null，即调用 lept_parse_null()函数
//2.如果传入的Json文本是空白的，那么函数会返回LEPT_PARSE_EXCEPT_VALUE
static int lept_parse_value(lept_context* c, lept_value* v) {
    switch (*c->json) {
    case 'n':
    case 'f':
    case 't':
        return lept_parse_iteral(c, v);
    case '\0': return LEPT_PARSE_EXPECT_VALUE;
    default: return lept_parse_number(c, v); 
    }
}
//解析一个Json文本。
int lept_parse(lept_value* v, const char* json) {
    lept_context c;
    int ret;
    assert(v != NULL);
    c.json = json;
    v->type = LEPT_NULL;
    lept_parse_whitespace(&c);
    if ((ret = lept_parse_value(&c, v)) == LEPT_PARSE_OK) {
        lept_parse_whitespace(&c);
        if (*c.json != '\0') {
            v->type = LEPT_NULL;
            ret = LEPT_PARSE_ROOT_NOT_SINGULAR;
        }
    }
    return ret;
}

//得到传入v的数据类型
lept_type lept_get_type(const lept_value* v) {
    assert(v != NULL);
    return v->type;
}
//当传入的json 类型是 LEPT_NUMBER，才能返回目标成员的数据
double lept_get_number(const lept_value* v)
{
    assert(v != NULL && v->type == LEPT_NUMBER);
    return v->n;
}

