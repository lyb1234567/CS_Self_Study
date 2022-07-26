#include "leptjson.h"
#include <assert.h>  /* assert() */
#include <stdlib.h>  /* NULL */

#define EXPECT(c, ch)       do { assert(*c->json == (ch)); c->json++; } while(0)

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
            v->type = LEPT_FALSE;
            return LEPT_PARSE_OK;
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
            v->type = LEPT_TRUE;
            return LEPT_PARSE_OK;
        }
        if (c->json[0] == ' ' && c->json[1] != '\0')
        {
            return LEPT_PARSE_ROOT_NOT_SINGULAR;
        }
        return LEPT_PARSE_INVALID_VALUE;
    }
}

//1.解析传入的json文本，如果开头是n,那么判断是否是null，即调用 lept_parse_null()函数
//2.如果传入的Json文本是空白的，那么函数会返回LEPT_PARSE_EXCEPT_VALUE
static int lept_parse_value(lept_context* c, lept_value* v) {
    switch (*c->json) {
    case 'n':  return lept_parse_null(c, v);
    case 'f':  return let_parse_false(c, v);
    case 't':  return let_parse_true(c, v);
    case '\0': return LEPT_PARSE_EXPECT_VALUE;
    default:   return LEPT_PARSE_INVALID_VALUE;
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

