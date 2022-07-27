#ifndef LEPTJSON_H_
#define LEPTJSON_H_

//设立Json的7种数据类型，并为其定义更为简介的声明类型
typedef enum {LEPT_NULL,LEPT_FALSE,LEPT_TRUE,LEPT_NUMBER,LEPT_STRING,LEPT_ARRAY,LEPT_OBJECT} lept_type;

// 构造一个Json值的结构体,该结构体目前包含7种数据类型
typedef struct
{
	lept_type type;
	double n;
}lept_value;


//解析函数会返回一下枚举值,该枚举值会反应不同的Json错误形式
//1.如果传入的Json文本格式是正确的，那么函数会返回LEPT_PARSE_OK
//2.如果传入的Json文本是空白的，那么函数会返回LEPT_PARSE_EXCEPT_VALUE
//3.若一个值之后，在空白之后还有其他字符，传回 LEPT_PARSE_ROOT_NOT_SINGULAR
//若值不是那三种字面值，传回 LEPT_PARSE_INVALID_VALUE。
enum
{
	LEPT_PARSE_OK = 0,
	LEPT_PARSE_INVALID_VALUE,
	LEPT_PARSE_EXPECT_VALUE,
	LEPT_PARSE_ROOT_NOT_SINGULAR,
	LEPT_PARSE_NUMBER_TOO_BIG

};
//解析Json,这个函数会用来解析Json文本，同时该文本不应该被我们手动改动，那么就应该是const char*
int lept_parse(lept_value* v, const char* json);
double lept_get_number(lept_value* v);
lept_type lept_get_type(const lept_value* v);
#endif 

#pragma once
