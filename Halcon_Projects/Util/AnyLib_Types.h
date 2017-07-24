#ifndef ANYLIB_TYPES_H
#define ANYLIB_TYPES_H



#ifndef __OS_INFO__
#define __OS_INFO__
#ifdef _WIN64
typedef long long Address_Ref;
#else
typedef long Address_Ref;
#endif
typedef Address_Ref Long;
#endif

#endif // ANYLIB_TYPES_H
