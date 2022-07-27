#include "leptjson.h"
#include <errno.h>
#include <math.h> 
#include <assert.h>  /* assert() */
#include <stdlib.h>  /* NULL */

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
    c->json = p;
}

//解析传入的文本是否是 “null”,如果传入的json文本不是“null”，则返回LEPT_PARSE_INVALID_VALUE。
//如果是，那么该json的数据类型就是null,然后返回LEPT_PARSE_OK,表示解析成功
static int lept_parse_null(lept_context* c, lept_value* v) {
    EXPECT(c, 'n');
    if (c->json[0] != 'u' || c->json[1] != 'l' || c->json[2] != 'l')
        return LEPT_PARSE_INVALID_VALUE;
    c->json += 3;
    if (c->json[0] =='\0')
    {
        v->type = LEPT_NULL;
        return LEPT_PARSE_OK;
    }
    else
    {
        if (c->json[0] == ' '&& c->json[1]=='\0')
        {
            v->type = LEPT_NULL;
            return LEPT_PARSE_OK;
        }
        if (c->json[0] == ' ' && c->json[1] != '\0')
        {
            return LEPT_PARSE_ROOT_NOT_SINGULAR;
        }
        return LEPT_PARSE_INVALID_VALUE;
    }
}

static int let_parse_false(lept_context* c, lept_value* v)
{
    EXPECT(c, 'f');
    if (c->json[0] != 'a' || c->json[1] != 'l' || c->json[2] != 's' || c->json[3] != 'e')
    {
        return  LEPT_PARSE_INVALID_VALUE;
    }
    c->json = c->json + 4;
    if (c->json[0] == '\0')
    {
        v->type = LEPT_FALSE;
        return LEPT_PARSE_OK;
    }
    else
    {
        if (c->json[0] == ' ' && c->json[1] == '\0')
        {
            return LEPT_PARSE_INVALID_VALUE;
        }
        if (c->json[0] == ' ' && c->json[1] != '\0')
        {
            return LEPT_PARSE_ROOT_NOT_SINGULAR;
        }
        return LEPT_PARSE_INVALID_VALUE;
    }
    

}

static int let_parse_true(lept_context* c, lept_value* v)
{
    EXPECT(c, 't');
    if (c->json[0] != 'r' || c->json[1] != 'u' || c->json[2] != 'e')
    {
        return LEPT_PARSE_INVALID_VALUE;
    }
    c->json = c->json + 3;
    if (c->json[0] == '\0')
    {
        v->type = LEPT_TRUE;
        return LEPT_PARSE_OK;
    }
    else
    {
        if (c->json[0] == ' ' && c->json[1] == '\0')
        {
            return LEPT_PARSE_INVALID_VALUE;
        }
        if (c->json[0] == ' ' && c->json[1] != '\0')
        {
            return LEPT_PARSE_ROOT_NOT_SINGULAR;
        }
        return LEPT_PARSE_INVALID_VALUE;
    }
}
static int lept_parse_number(lept_context* c, lept_value* v)
{
    //首先判断是开头为 0 还是'-'号，如果是其中一个，那么就可以继续解析，否则就解析失败
    const char* p = c->json;
    // *p为字符串字母，然后开始下一位
    if (*p == '0')
    {
        if (p[1] == '\0')
        {
            v->n = strtod(c->json, NULL);
            v->type = LEPT_NUMBER;
            c->json = p;
            return LEPT_PARSE_OK;
        }
        if (p[1] == '.')
        {
            p++;
        }
        else
        {
            return LEPT_PARSE_INVALID_VALUE;
        }

    }
    if (*p == '-')
        p++;
    //得到下一个字符之后，不管是首字符是'-'号还是0，如果下一个字符不是1-9中的字符，那么就代表这个不是个标准数字
    else
    {
        //用于检验下一个字符是否是规范字符
        if (!ISDIGIT1TO9(*p))
        {
            return LEPT_PARSE_INVALID_VALUE;
        }
        //检查下一个字符是否为0~9,因为之前已经检查第三位是1-9的数字，那么我们就第四位开始遍历后续字符串，如果遇到不是0-9的数字就跳出循环
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
    case 'n':  return lept_parse_null(c, v);
    case 'f':  return let_parse_false(c, v);
    case 't':  return let_parse_true(c, v);
    case '\0': return LEPT_PARSE_EXPECT_VALUE;
    default:   return lept_parse_number(c, v);
    }
}
//解析一个Json文本。
int lept_parse(lept_value* v, const char* json) {
    lept_context c;
    assert(v != NULL);
    c.json = json;
    //如果后续没能解析成功，那么该json v的数据类型就保持为LEPT_NULL不变
    v->type = LEPT_NULL;
    lept_parse_whitespace(&c);
    return lept_parse_value(&c, v);
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

