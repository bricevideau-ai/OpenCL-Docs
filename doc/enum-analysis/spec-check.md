# SPEC DISCOVERY — unassigned cl.xml tokens (manual check)

365 tokens.  Mark each as: assign `group=...` / confirm ungrouped.

## `CL_CHAR_BIT`  (container: `Constants`, value: 8)
- `api/appendix_c.asciidoc`:
     
     [width="100%",cols="<50%,<50%"]
     |====
  >> | {CL_CHAR_BIT_anchor}
     
     [version-note]
     | Bit width of a character
- `api/appendix_c.asciidoc`:
     |====
     | {CL_CHAR_BIT_anchor}
     
  >> [version-note]
     | Bit width of a character
     | {CL_SCHAR_MAX_anchor}
     

## `CL_CHAR_MAX`  (container: `Constants`, value: CL_SCHAR_MAX)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Minimum value of a type {cl_char_TYPE}
  >> | {CL_CHAR_MAX_anchor}
     
     [version-note]
     | Maximum value of a type {cl_char_TYPE}
- `api/appendix_c.asciidoc`:
     | Minimum value of a type {cl_char_TYPE}
     | {CL_CHAR_MAX_anchor}
     
  >> [version-note]
     | Maximum value of a type {cl_char_TYPE}
     | {CL_CHAR_MIN_anchor}
     

## `CL_CHAR_MIN`  (container: `Constants`, value: CL_SCHAR_MIN)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of a type {cl_char_TYPE}
  >> | {CL_CHAR_MIN_anchor}
     
     [version-note]
     | Minimum value of a type {cl_char_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of a type {cl_char_TYPE}
     | {CL_CHAR_MIN_anchor}
     
  >> [version-note]
     | Minimum value of a type {cl_char_TYPE}
     | {CL_UCHAR_MAX_anchor}
     

## `CL_DBL_DIG`  (container: `Constants`, value: 15)
- `api/appendix_c.asciidoc`:
     [version-note]
     | Minimum positive floating-point number of type {cl_float_TYPE} such that `1.0
     {plus} {CL_FLT_EPSILON} != 1` is true.
  >> | {CL_DBL_DIG_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     {plus} {CL_FLT_EPSILON} != 1` is true.
     | {CL_DBL_DIG_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Number of decimal digits of precision for the type {cl_double_TYPE}
     | {CL_DBL_MANT_DIG_anchor}

## `CL_DBL_EPSILON`  (container: `Constants`, value: 2.220446049250313080847e-16)
- `api/appendix_c.asciidoc`:
     [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Minimum value of type {cl_double_TYPE}
  >> | {CL_DBL_EPSILON_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     | Minimum value of type {cl_double_TYPE}
     | {CL_DBL_EPSILON_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Minimum positive floating-point number of type {cl_double_TYPE} such that
     `1.0 {plus} {CL_DBL_EPSILON} != 1` is true.
- `api/appendix_c.asciidoc`:
     [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Minimum positive floating-point number of type {cl_double_TYPE} such that
  >> `1.0 {plus} {CL_DBL_EPSILON} != 1` is true.
     | {CL_NAN_anchor}
     
     [version-note]

## `CL_DBL_MANT_DIG`  (container: `Constants`, value: 53)
- `api/appendix_c.asciidoc`:
     [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Number of decimal digits of precision for the type {cl_double_TYPE}
  >> | {CL_DBL_MANT_DIG_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     | Number of decimal digits of precision for the type {cl_double_TYPE}
     | {CL_DBL_MANT_DIG_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Number of digits in the mantissa of type {cl_double_TYPE}
     | {CL_DBL_MAX_10_EXP_anchor}

## `CL_DBL_MAX`  (container: `Constants`, value: 1.7976931348623158e+308)
- `api/appendix_c.asciidoc`:
     [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Base value of type {cl_double_TYPE}
  >> | {CL_DBL_MAX_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     | Base value of type {cl_double_TYPE}
     | {CL_DBL_MAX_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Maximum value of type {cl_double_TYPE}
     | {CL_DBL_MIN_anchor}

## `CL_DBL_MAX_10_EXP`  (container: `Constants`, value: +308)
- `api/appendix_c.asciidoc`:
     [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Number of digits in the mantissa of type {cl_double_TYPE}
  >> | {CL_DBL_MAX_10_EXP_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     | Number of digits in the mantissa of type {cl_double_TYPE}
     | {CL_DBL_MAX_10_EXP_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Maximum positive integer such that 10 raised to this power minus one can
     be represented as a normalized floating-point number of type {cl_double_TYPE}

## `CL_DBL_MAX_EXP`  (container: `Constants`, value: +1024)
- `api/appendix_c.asciidoc`:
     Also see {cl_khr_fp64_EXT}.
     | Maximum positive integer such that 10 raised to this power minus one can
     be represented as a normalized floating-point number of type {cl_double_TYPE}
  >> | {CL_DBL_MAX_EXP_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     be represented as a normalized floating-point number of type {cl_double_TYPE}
     | {CL_DBL_MAX_EXP_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Maximum exponent value of type {cl_double_TYPE}
     | {CL_DBL_MIN_10_EXP_anchor}

## `CL_DBL_MIN`  (container: `Constants`, value: 2.225073858507201383090e-308)
- `api/appendix_c.asciidoc`:
     [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Maximum value of type {cl_double_TYPE}
  >> | {CL_DBL_MIN_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     | Maximum value of type {cl_double_TYPE}
     | {CL_DBL_MIN_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Minimum value of type {cl_double_TYPE}
     | {CL_DBL_EPSILON_anchor}

## `CL_DBL_MIN_10_EXP`  (container: `Constants`, value: -307)
- `api/appendix_c.asciidoc`:
     [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Maximum exponent value of type {cl_double_TYPE}
  >> | {CL_DBL_MIN_10_EXP_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     | Maximum exponent value of type {cl_double_TYPE}
     | {CL_DBL_MIN_10_EXP_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Minimum negative integer such that 10 raised to this power minus one can
     be represented as a normalized floating-point number of type {cl_double_TYPE}

## `CL_DBL_MIN_EXP`  (container: `Constants`, value: -1021)
- `api/appendix_c.asciidoc`:
     Also see {cl_khr_fp64_EXT}.
     | Minimum negative integer such that 10 raised to this power minus one can
     be represented as a normalized floating-point number of type {cl_double_TYPE}
  >> | {CL_DBL_MIN_EXP_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     be represented as a normalized floating-point number of type {cl_double_TYPE}
     | {CL_DBL_MIN_EXP_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Minimum exponent value of type {cl_double_TYPE}
     | {CL_DBL_RADIX_anchor}

## `CL_DBL_RADIX`  (container: `Constants`, value: 2)
- `api/appendix_c.asciidoc`:
     [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Minimum exponent value of type {cl_double_TYPE}
  >> | {CL_DBL_RADIX_anchor}
     
     [version-note]
     Also see {cl_khr_fp64_EXT}.
- `api/appendix_c.asciidoc`:
     | Minimum exponent value of type {cl_double_TYPE}
     | {CL_DBL_RADIX_anchor}
     
  >> [version-note]
     Also see {cl_khr_fp64_EXT}.
     | Base value of type {cl_double_TYPE}
     | {CL_DBL_MAX_anchor}

## `CL_FLT_DIG`  (container: `Constants`, value: 6)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of a type {cl_ulong_TYPE}
  >> | {CL_FLT_DIG_anchor}
     
     [version-note]
     | Number of decimal digits of precision for the type {cl_float_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of a type {cl_ulong_TYPE}
     | {CL_FLT_DIG_anchor}
     
  >> [version-note]
     | Number of decimal digits of precision for the type {cl_float_TYPE}
     | {CL_FLT_MANT_DIG_anchor}
     

## `CL_FLT_EPSILON`  (container: `Constants`, value: 1.1920928955078125e-7f)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Minimum value of type {cl_float_TYPE}
  >> | {CL_FLT_EPSILON_anchor}
     
     [version-note]
     | Minimum positive floating-point number of type {cl_float_TYPE} such that `1.0
- `api/appendix_c.asciidoc`:
     | Minimum value of type {cl_float_TYPE}
     | {CL_FLT_EPSILON_anchor}
     
  >> [version-note]
     | Minimum positive floating-point number of type {cl_float_TYPE} such that `1.0
     {plus} {CL_FLT_EPSILON} != 1` is true.
     | {CL_DBL_DIG_anchor}
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Minimum positive floating-point number of type {cl_float_TYPE} such that `1.0
  >> {plus} {CL_FLT_EPSILON} != 1` is true.
     | {CL_DBL_DIG_anchor}
     
     [version-note]

## `CL_FLT_MANT_DIG`  (container: `Constants`, value: 24)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Number of decimal digits of precision for the type {cl_float_TYPE}
  >> | {CL_FLT_MANT_DIG_anchor}
     
     [version-note]
     | Number of digits in the mantissa of type {cl_float_TYPE}
- `api/appendix_c.asciidoc`:
     | Number of decimal digits of precision for the type {cl_float_TYPE}
     | {CL_FLT_MANT_DIG_anchor}
     
  >> [version-note]
     | Number of digits in the mantissa of type {cl_float_TYPE}
     | {CL_FLT_MAX_10_EXP_anchor}
     

## `CL_FLT_MAX`  (container: `Constants`, value: 340282346638528859811704183484516925440.0f)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Base value of type {cl_float_TYPE}
  >> | {CL_FLT_MAX_anchor}
     
     [version-note]
     | Maximum value of type {cl_float_TYPE}
- `api/appendix_c.asciidoc`:
     | Base value of type {cl_float_TYPE}
     | {CL_FLT_MAX_anchor}
     
  >> [version-note]
     | Maximum value of type {cl_float_TYPE}
     | {CL_FLT_MIN_anchor}
     

## `CL_FLT_MAX_10_EXP`  (container: `Constants`, value: +38)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Number of digits in the mantissa of type {cl_float_TYPE}
  >> | {CL_FLT_MAX_10_EXP_anchor}
     
     [version-note]
     | Maximum positive integer such that 10 raised to this power minus one can
- `api/appendix_c.asciidoc`:
     | Number of digits in the mantissa of type {cl_float_TYPE}
     | {CL_FLT_MAX_10_EXP_anchor}
     
  >> [version-note]
     | Maximum positive integer such that 10 raised to this power minus one can
     be represented as a normalized floating-point number of type {cl_float_TYPE}
     | {CL_FLT_MAX_EXP_anchor}

## `CL_FLT_MAX_EXP`  (container: `Constants`, value: +128)
- `api/appendix_c.asciidoc`:
     [version-note]
     | Maximum positive integer such that 10 raised to this power minus one can
     be represented as a normalized floating-point number of type {cl_float_TYPE}
  >> | {CL_FLT_MAX_EXP_anchor}
     
     [version-note]
     | Maximum exponent value of type {cl_float_TYPE}
- `api/appendix_c.asciidoc`:
     be represented as a normalized floating-point number of type {cl_float_TYPE}
     | {CL_FLT_MAX_EXP_anchor}
     
  >> [version-note]
     | Maximum exponent value of type {cl_float_TYPE}
     | {CL_FLT_MIN_10_EXP_anchor}
     

## `CL_FLT_MIN`  (container: `Constants`, value: 1.175494350822287507969e-38f)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of type {cl_float_TYPE}
  >> | {CL_FLT_MIN_anchor}
     
     [version-note]
     | Minimum value of type {cl_float_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of type {cl_float_TYPE}
     | {CL_FLT_MIN_anchor}
     
  >> [version-note]
     | Minimum value of type {cl_float_TYPE}
     | {CL_FLT_EPSILON_anchor}
     

## `CL_FLT_MIN_10_EXP`  (container: `Constants`, value: -37)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum exponent value of type {cl_float_TYPE}
  >> | {CL_FLT_MIN_10_EXP_anchor}
     
     [version-note]
     | Minimum negative integer such that 10 raised to this power minus one can
- `api/appendix_c.asciidoc`:
     | Maximum exponent value of type {cl_float_TYPE}
     | {CL_FLT_MIN_10_EXP_anchor}
     
  >> [version-note]
     | Minimum negative integer such that 10 raised to this power minus one can
     be represented as a normalized floating-point number of type {cl_float_TYPE}
     | {CL_FLT_MIN_EXP_anchor}

## `CL_FLT_MIN_EXP`  (container: `Constants`, value: -125)
- `api/appendix_c.asciidoc`:
     [version-note]
     | Minimum negative integer such that 10 raised to this power minus one can
     be represented as a normalized floating-point number of type {cl_float_TYPE}
  >> | {CL_FLT_MIN_EXP_anchor}
     
     [version-note]
     | Minimum exponent value of type {cl_float_TYPE}
- `api/appendix_c.asciidoc`:
     be represented as a normalized floating-point number of type {cl_float_TYPE}
     | {CL_FLT_MIN_EXP_anchor}
     
  >> [version-note]
     | Minimum exponent value of type {cl_float_TYPE}
     | {CL_FLT_RADIX_anchor}
     

## `CL_FLT_RADIX`  (container: `Constants`, value: 2)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Minimum exponent value of type {cl_float_TYPE}
  >> | {CL_FLT_RADIX_anchor}
     
     [version-note]
     | Base value of type {cl_float_TYPE}
- `api/appendix_c.asciidoc`:
     | Minimum exponent value of type {cl_float_TYPE}
     | {CL_FLT_RADIX_anchor}
     
  >> [version-note]
     | Base value of type {cl_float_TYPE}
     | {CL_FLT_MAX_anchor}
     

## `CL_HALF_DIG`  (container: `Constants`, value: 3)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HALF_EPSILON`  (container: `Constants`, value: 9.765625e-04f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HALF_MANT_DIG`  (container: `Constants`, value: 11)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HALF_MAX`  (container: `Constants`, value: 65504.0f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HALF_MAX_10_EXP`  (container: `Constants`, value: +4)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HALF_MAX_EXP`  (container: `Constants`, value: +16)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HALF_MIN`  (container: `Constants`, value: 6.103515625e-05f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HALF_MIN_10_EXP`  (container: `Constants`, value: -4)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HALF_MIN_EXP`  (container: `Constants`, value: -13)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HALF_RADIX`  (container: `Constants`, value: 2)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_HUGE_VAL`  (container: `Constants`, value: ((cl_double) 1e500))
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Largest representative value of type {cl_float_TYPE}
  >> | {CL_HUGE_VAL_anchor}
     
     [version-note]
     | Largest representative value of type {cl_double_TYPE}
- `api/appendix_c.asciidoc`:
     | Largest representative value of type {cl_float_TYPE}
     | {CL_HUGE_VAL_anchor}
     
  >> [version-note]
     | Largest representative value of type {cl_double_TYPE}
     | {CL_MAXFLOAT_anchor}
     

## `CL_HUGE_VALF`  (container: `Constants`, value: ((cl_float) 1e50))
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Macro expanding to a value representing NaN
  >> | {CL_HUGE_VALF_anchor}
     
     [version-note]
     | Largest representative value of type {cl_float_TYPE}
- `api/appendix_c.asciidoc`:
     | Macro expanding to a value representing NaN
     | {CL_HUGE_VALF_anchor}
     
  >> [version-note]
     | Largest representative value of type {cl_float_TYPE}
     | {CL_HUGE_VAL_anchor}
     

## `CL_INFINITY`  (container: `Constants`, value: CL_HUGE_VALF)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of type {cl_float_TYPE}
  >> | {CL_INFINITY_anchor}
     
     [version-note]
     | Macro expanding to a value representing infinity
- `api/appendix_c.asciidoc`:
     | Maximum value of type {cl_float_TYPE}
     | {CL_INFINITY_anchor}
     
  >> [version-note]
     | Macro expanding to a value representing infinity
     |====
     

## `CL_INT_MAX`  (container: `Constants`, value: 2147483647)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of a type {cl_ushort_TYPE}
  >> | {CL_INT_MAX_anchor}
     
     [version-note]
     | Maximum value of a type {cl_int_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of a type {cl_ushort_TYPE}
     | {CL_INT_MAX_anchor}
     
  >> [version-note]
     | Maximum value of a type {cl_int_TYPE}
     | {CL_INT_MIN_anchor}
     

## `CL_INT_MIN`  (container: `Constants`, value: (-2147483647-1))
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of a type {cl_int_TYPE}
  >> | {CL_INT_MIN_anchor}
     
     [version-note]
     | Minimum value of a type {cl_int_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of a type {cl_int_TYPE}
     | {CL_INT_MIN_anchor}
     
  >> [version-note]
     | Minimum value of a type {cl_int_TYPE}
     | {CL_UINT_MAX_anchor}
     

## `CL_LONG_MAX`  (container: `Constants`, value: ((cl_long) 0x7FFFFFFFFFFFFFFFLL))
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of a type {cl_uint_TYPE}
  >> | {CL_LONG_MAX_anchor}
     
     [version-note]
     | Maximum value of a type {cl_long_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of a type {cl_uint_TYPE}
     | {CL_LONG_MAX_anchor}
     
  >> [version-note]
     | Maximum value of a type {cl_long_TYPE}
     | {CL_LONG_MIN_anchor}
     

## `CL_LONG_MIN`  (container: `Constants`, value: ((cl_long) -0x7FFFFFFFFFFFFFFFLL - 1LL))
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of a type {cl_long_TYPE}
  >> | {CL_LONG_MIN_anchor}
     
     [version-note]
     | Minimum value of a type {cl_long_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of a type {cl_long_TYPE}
     | {CL_LONG_MIN_anchor}
     
  >> [version-note]
     | Minimum value of a type {cl_long_TYPE}
     | {CL_ULONG_MAX_anchor}
     

## `CL_MAXFLOAT`  (container: `Constants`, value: CL_FLT_MAX)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Largest representative value of type {cl_double_TYPE}
  >> | {CL_MAXFLOAT_anchor}
     
     [version-note]
     | Maximum value of type {cl_float_TYPE}
- `api/appendix_c.asciidoc`:
     | Largest representative value of type {cl_double_TYPE}
     | {CL_MAXFLOAT_anchor}
     
  >> [version-note]
     | Maximum value of type {cl_float_TYPE}
     | {CL_INFINITY_anchor}
     

## `CL_M_1_PI`  (container: `Constants`, value: 0.31830988618379067154)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_1_PI_F`  (container: `Constants`, value: 0.318309886f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_2_PI`  (container: `Constants`, value: 0.63661977236758134308)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_2_PI_F`  (container: `Constants`, value: 0.636619772f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_2_SQRTPI`  (container: `Constants`, value: 1.12837916709551257390)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_2_SQRTPI_F`  (container: `Constants`, value: 1.128379167f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_E`  (container: `Constants`, value: 2.7182818284590452354)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_E_F`  (container: `Constants`, value: 2.718281828f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_LN10`  (container: `Constants`, value: 2.30258509299404568402)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_LN10_F`  (container: `Constants`, value: 2.302585093f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_LN2`  (container: `Constants`, value: 0.69314718055994530942)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_LN2_F`  (container: `Constants`, value: 0.693147181f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_LOG10E`  (container: `Constants`, value: 0.43429448190325182765)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_LOG10E_F`  (container: `Constants`, value: 0.434294482f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_LOG2E`  (container: `Constants`, value: 1.4426950408889634074)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_LOG2E_F`  (container: `Constants`, value: 1.442695041f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_PI`  (container: `Constants`, value: 3.14159265358979323846)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_PI_2`  (container: `Constants`, value: 1.57079632679489661923)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_PI_2_F`  (container: `Constants`, value: 1.570796327f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_PI_4`  (container: `Constants`, value: 0.78539816339744830962)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_PI_4_F`  (container: `Constants`, value: 0.785398163f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_PI_F`  (container: `Constants`, value: 3.141592654f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_SQRT1_2`  (container: `Constants`, value: 0.70710678118654752440)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_SQRT1_2_F`  (container: `Constants`, value: 0.707106781f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_SQRT2`  (container: `Constants`, value: 1.41421356237309504880)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_M_SQRT2_F`  (container: `Constants`, value: 1.414213562f)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_NAN`  (container: `Constants`, value: (CL_INFINITY - CL_INFINITY))
- `api/appendix_c.asciidoc`:
     Also see {cl_khr_fp64_EXT}.
     | Minimum positive floating-point number of type {cl_double_TYPE} such that
     `1.0 {plus} {CL_DBL_EPSILON} != 1` is true.
  >> | {CL_NAN_anchor}
     
     [version-note]
     | Macro expanding to a value representing NaN
- `api/appendix_c.asciidoc`:
     `1.0 {plus} {CL_DBL_EPSILON} != 1` is true.
     | {CL_NAN_anchor}
     
  >> [version-note]
     | Macro expanding to a value representing NaN
     | {CL_HUGE_VALF_anchor}
     

## `CL_SCHAR_MAX`  (container: `Constants`, value: 127)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Bit width of a character
  >> | {CL_SCHAR_MAX_anchor}
     
     [version-note]
     | Maximum value of a type {cl_char_TYPE}
- `api/appendix_c.asciidoc`:
     | Bit width of a character
     | {CL_SCHAR_MAX_anchor}
     
  >> [version-note]
     | Maximum value of a type {cl_char_TYPE}
     | {CL_SCHAR_MIN_anchor}
     

## `CL_SCHAR_MIN`  (container: `Constants`, value: (-127-1))
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of a type {cl_char_TYPE}
  >> | {CL_SCHAR_MIN_anchor}
     
     [version-note]
     | Minimum value of a type {cl_char_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of a type {cl_char_TYPE}
     | {CL_SCHAR_MIN_anchor}
     
  >> [version-note]
     | Minimum value of a type {cl_char_TYPE}
     | {CL_CHAR_MAX_anchor}
     

## `CL_SHRT_MAX`  (container: `Constants`, value: 32767)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of a type {cl_uchar_TYPE}
  >> | {CL_SHRT_MAX_anchor}
     
     [version-note]
     | Maximum value of a type {cl_short_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of a type {cl_uchar_TYPE}
     | {CL_SHRT_MAX_anchor}
     
  >> [version-note]
     | Maximum value of a type {cl_short_TYPE}
     | {CL_SHRT_MIN_anchor}
     

## `CL_SHRT_MIN`  (container: `Constants`, value: (-32767-1))
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Maximum value of a type {cl_short_TYPE}
  >> | {CL_SHRT_MIN_anchor}
     
     [version-note]
     | Minimum value of a type {cl_short_TYPE}
- `api/appendix_c.asciidoc`:
     | Maximum value of a type {cl_short_TYPE}
     | {CL_SHRT_MIN_anchor}
     
  >> [version-note]
     | Minimum value of a type {cl_short_TYPE}
     | {CL_USHRT_MAX_anchor}
     

## `CL_UCHAR_MAX`  (container: `Constants`, value: 255)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Minimum value of a type {cl_char_TYPE}
  >> | {CL_UCHAR_MAX_anchor}
     
     [version-note]
     | Maximum value of a type {cl_uchar_TYPE}
- `api/appendix_c.asciidoc`:
     | Minimum value of a type {cl_char_TYPE}
     | {CL_UCHAR_MAX_anchor}
     
  >> [version-note]
     | Maximum value of a type {cl_uchar_TYPE}
     | {CL_SHRT_MAX_anchor}
     

## `CL_UINT_MAX`  (container: `Constants`, value: 0xffffffffU)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Minimum value of a type {cl_int_TYPE}
  >> | {CL_UINT_MAX_anchor}
     
     [version-note]
     | Maximum value of a type {cl_uint_TYPE}
- `api/appendix_c.asciidoc`:
     | Minimum value of a type {cl_int_TYPE}
     | {CL_UINT_MAX_anchor}
     
  >> [version-note]
     | Maximum value of a type {cl_uint_TYPE}
     | {CL_LONG_MAX_anchor}
     
- `api/cl_khr_command_buffer.asciidoc`:
     
     The {cl_sync_point_khr_TYPE} type is defined as a `cl_uint`, giving a hard
     upper limit on the number of commands a command-buffer can hold as
  >> {CL_UINT_MAX}, at which point {CL_OUT_OF_RESOURCES} will be returned. However,
     it is likely an implementation will reach capacity before this threshold is
     hit.
     

## `CL_ULONG_MAX`  (container: `Constants`, value: ((cl_ulong) 0xFFFFFFFFFFFFFFFFULL))
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Minimum value of a type {cl_long_TYPE}
  >> | {CL_ULONG_MAX_anchor}
     
     [version-note]
     | Maximum value of a type {cl_ulong_TYPE}
- `api/appendix_c.asciidoc`:
     | Minimum value of a type {cl_long_TYPE}
     | {CL_ULONG_MAX_anchor}
     
  >> [version-note]
     | Maximum value of a type {cl_ulong_TYPE}
     | {CL_FLT_DIG_anchor}
     

## `CL_USHRT_MAX`  (container: `Constants`, value: 65535)
- `api/appendix_c.asciidoc`:
     
     [version-note]
     | Minimum value of a type {cl_short_TYPE}
  >> | {CL_USHRT_MAX_anchor}
     
     [version-note]
     | Maximum value of a type {cl_ushort_TYPE}
- `api/appendix_c.asciidoc`:
     | Minimum value of a type {cl_short_TYPE}
     | {CL_USHRT_MAX_anchor}
     
  >> [version-note]
     | Maximum value of a type {cl_ushort_TYPE}
     | {CL_INT_MAX_anchor}
     

## `CL_NAME_VERSION_MAX_NAME_SIZE`  (container: `Constants.Versioning`, value: 64)
- `api/opencl_architecture.asciidoc`:
     [version-note]
     
     * _version_ is a <<version-numbers, Version Number>>.
  >> * _name_ is an array of {CL_NAME_VERSION_MAX_NAME_SIZE_anchor} characters
     containing a null-terminated string, whose maximum length is therefore
     {CL_NAME_VERSION_MAX_NAME_SIZE} minus one.
     --
- `api/opencl_architecture.asciidoc`:
     * _version_ is a <<version-numbers, Version Number>>.
     * _name_ is an array of {CL_NAME_VERSION_MAX_NAME_SIZE_anchor} characters
     containing a null-terminated string, whose maximum length is therefore
  >> {CL_NAME_VERSION_MAX_NAME_SIZE} minus one.
     --
     
     [[valid-usage]]

## `CL_VERSION_MAJOR_BITS`  (container: `Constants.Versioning`, value: 10)
- `api/opencl_architecture.asciidoc`:
     {cl_version_TYPE}.
     * {CL_MAKE_VERSION_anchor} returns a packed {cl_version_TYPE} from a
     _major_, _minor_ and _patch_ version.
  >> * {CL_VERSION_MAJOR_BITS_anchor}, {CL_VERSION_MINOR_BITS_anchor}, and
     {CL_VERSION_PATCH_BITS_anchor} are the number of bits in the
     corresponding field.
     * {CL_VERSION_MAJOR_MASK_anchor}, {CL_VERSION_MINOR_MASK_anchor}, and
- `api/opencl_architecture.asciidoc`:
     ----
     typedef cl_uint cl_version;
     
  >> #define CL_VERSION_MAJOR_BITS (10)
     #define CL_VERSION_MINOR_BITS (10)
     #define CL_VERSION_PATCH_BITS (12)
     
- `api/opencl_architecture.asciidoc`:
     #define CL_VERSION_MINOR_BITS (10)
     #define CL_VERSION_PATCH_BITS (12)
     
  >> #define CL_VERSION_MAJOR_MASK ((1 << CL_VERSION_MAJOR_BITS) - 1)
     #define CL_VERSION_MINOR_MASK ((1 << CL_VERSION_MINOR_BITS) - 1)
     #define CL_VERSION_PATCH_MASK ((1 << CL_VERSION_PATCH_BITS) - 1)
     

## `CL_VERSION_MINOR_BITS`  (container: `Constants.Versioning`, value: 10)
- `api/opencl_architecture.asciidoc`:
     {cl_version_TYPE}.
     * {CL_MAKE_VERSION_anchor} returns a packed {cl_version_TYPE} from a
     _major_, _minor_ and _patch_ version.
  >> * {CL_VERSION_MAJOR_BITS_anchor}, {CL_VERSION_MINOR_BITS_anchor}, and
     {CL_VERSION_PATCH_BITS_anchor} are the number of bits in the
     corresponding field.
     * {CL_VERSION_MAJOR_MASK_anchor}, {CL_VERSION_MINOR_MASK_anchor}, and
- `api/opencl_architecture.asciidoc`:
     typedef cl_uint cl_version;
     
     #define CL_VERSION_MAJOR_BITS (10)
  >> #define CL_VERSION_MINOR_BITS (10)
     #define CL_VERSION_PATCH_BITS (12)
     
     #define CL_VERSION_MAJOR_MASK ((1 << CL_VERSION_MAJOR_BITS) - 1)
- `api/opencl_architecture.asciidoc`:
     #define CL_VERSION_PATCH_BITS (12)
     
     #define CL_VERSION_MAJOR_MASK ((1 << CL_VERSION_MAJOR_BITS) - 1)
  >> #define CL_VERSION_MINOR_MASK ((1 << CL_VERSION_MINOR_BITS) - 1)
     #define CL_VERSION_PATCH_MASK ((1 << CL_VERSION_PATCH_BITS) - 1)
     
     #define CL_VERSION_MAJOR(version) \
- `api/opencl_architecture.asciidoc`:
     #define CL_VERSION_PATCH_MASK ((1 << CL_VERSION_PATCH_BITS) - 1)
     
     #define CL_VERSION_MAJOR(version) \
  >> ((version) >> (CL_VERSION_MINOR_BITS + CL_VERSION_PATCH_BITS))
     
     #define CL_VERSION_MINOR(version) \
     (((version) >> CL_VERSION_PATCH_BITS) & CL_VERSION_MINOR_MASK)
- `api/opencl_architecture.asciidoc`:
     
     #define CL_MAKE_VERSION(major, minor, patch) \
     ((((major) & CL_VERSION_MAJOR_MASK) << \
  >> (CL_VERSION_MINOR_BITS + CL_VERSION_PATCH_BITS)) | \
     (((minor) & CL_VERSION_MINOR_MASK) << \
     CL_VERSION_PATCH_BITS) | \
     ((patch) & CL_VERSION_PATCH_MASK))

## `CL_VERSION_PATCH_BITS`  (container: `Constants.Versioning`, value: 12)
- `api/opencl_architecture.asciidoc`:
     * {CL_MAKE_VERSION_anchor} returns a packed {cl_version_TYPE} from a
     _major_, _minor_ and _patch_ version.
     * {CL_VERSION_MAJOR_BITS_anchor}, {CL_VERSION_MINOR_BITS_anchor}, and
  >> {CL_VERSION_PATCH_BITS_anchor} are the number of bits in the
     corresponding field.
     * {CL_VERSION_MAJOR_MASK_anchor}, {CL_VERSION_MINOR_MASK_anchor}, and
     {CL_VERSION_PATCH_MASK_anchor} are bitmasks used to extract the
- `api/opencl_architecture.asciidoc`:
     
     #define CL_VERSION_MAJOR_BITS (10)
     #define CL_VERSION_MINOR_BITS (10)
  >> #define CL_VERSION_PATCH_BITS (12)
     
     #define CL_VERSION_MAJOR_MASK ((1 << CL_VERSION_MAJOR_BITS) - 1)
     #define CL_VERSION_MINOR_MASK ((1 << CL_VERSION_MINOR_BITS) - 1)
- `api/opencl_architecture.asciidoc`:
     
     #define CL_VERSION_MAJOR_MASK ((1 << CL_VERSION_MAJOR_BITS) - 1)
     #define CL_VERSION_MINOR_MASK ((1 << CL_VERSION_MINOR_BITS) - 1)
  >> #define CL_VERSION_PATCH_MASK ((1 << CL_VERSION_PATCH_BITS) - 1)
     
     #define CL_VERSION_MAJOR(version) \
     ((version) >> (CL_VERSION_MINOR_BITS + CL_VERSION_PATCH_BITS))
- `api/opencl_architecture.asciidoc`:
     #define CL_VERSION_PATCH_MASK ((1 << CL_VERSION_PATCH_BITS) - 1)
     
     #define CL_VERSION_MAJOR(version) \
  >> ((version) >> (CL_VERSION_MINOR_BITS + CL_VERSION_PATCH_BITS))
     
     #define CL_VERSION_MINOR(version) \
     (((version) >> CL_VERSION_PATCH_BITS) & CL_VERSION_MINOR_MASK)
- `api/opencl_architecture.asciidoc`:
     ((version) >> (CL_VERSION_MINOR_BITS + CL_VERSION_PATCH_BITS))
     
     #define CL_VERSION_MINOR(version) \
  >> (((version) >> CL_VERSION_PATCH_BITS) & CL_VERSION_MINOR_MASK)
     
     #define CL_VERSION_PATCH(version) ((version) & CL_VERSION_PATCH_MASK)
     
- `api/opencl_architecture.asciidoc`:
     
     #define CL_MAKE_VERSION(major, minor, patch) \
     ((((major) & CL_VERSION_MAJOR_MASK) << \
  >> (CL_VERSION_MINOR_BITS + CL_VERSION_PATCH_BITS)) | \
     (((minor) & CL_VERSION_MINOR_MASK) << \
     CL_VERSION_PATCH_BITS) | \
     ((patch) & CL_VERSION_PATCH_MASK))

## `CL_IMPORT_MEMORY_WHOLE_ALLOCATION_ARM`  (container: `Constants.cl_arm_import_memory`, value: SIZE_MAX)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_LUID_SIZE_KHR`  (container: `Constants.cl_khr_device_uuid`, value: 8)
- `api/cl_khr_device_uuid.asciidoc`:
     * Constants describing the size of the driver and device UUIDs, and the
     device LUID:
     ** {CL_UUID_SIZE_KHR}
  >> ** {CL_LUID_SIZE_KHR}
     
     === Version History
     
- `api/opencl_platform_layer.asciidoc`:
     endif::cl_khr_device_uuid[]
     | {cl_uchar_TYPE}[{CL_LUID_SIZE}]
     
  >> ifdef::cl_khr_device_uuid[or {cl_uchar_TYPE}[{CL_LUID_SIZE_KHR}]]
     | Returns a locally unique identifier (LUID) for the device.
     
     It is not an error to query {CL_DEVICE_LUID}
- `api/opencl_platform_layer.asciidoc`:
     object and must be equal to the locally unique identifier of an
     `IDXGIAdapter1` object that corresponds to the OpenCL device.
     
  >> {CL_LUID_SIZE_KHR_anchor}
     ifdef::cl_khr_device_uuid[or {CL_LUID_SIZE_KHR_anchor}]
     is the size of the LUID, in bytes.
     | {CL_DEVICE_NODE_MASK_anchor}
- `api/opencl_platform_layer.asciidoc`:
     `IDXGIAdapter1` object that corresponds to the OpenCL device.
     
     {CL_LUID_SIZE_KHR_anchor}
  >> ifdef::cl_khr_device_uuid[or {CL_LUID_SIZE_KHR_anchor}]
     is the size of the LUID, in bytes.
     | {CL_DEVICE_NODE_MASK_anchor}
     

## `CL_UUID_SIZE_KHR`  (container: `Constants.cl_khr_device_uuid`, value: 16)
- `api/cl_khr_device_uuid.asciidoc`:
     ** {CL_DEVICE_NODE_MASK_KHR}
     * Constants describing the size of the driver and device UUIDs, and the
     device LUID:
  >> ** {CL_UUID_SIZE_KHR}
     ** {CL_LUID_SIZE_KHR}
     
     === Version History
- `api/opencl_platform_layer.asciidoc`:
     endif::cl_khr_device_uuid[]
     | {cl_uchar_TYPE}[{CL_UUID_SIZE}]
     
  >> ifdef::cl_khr_device_uuid[or {cl_uchar_TYPE}[{CL_UUID_SIZE_KHR}]]
     | Returns a universally unique identifier (UUID) for the device.
     
     Device UUIDs must be immutable for a given device across processes,
- `api/opencl_platform_layer.asciidoc`:
     driver APIs, driver versions, and system reboots.
     
     {CL_UUID_SIZE_anchor}
  >> ifdef::cl_khr_device_uuid[or {CL_UUID_SIZE_KHR_anchor}]
     is the size of the UUID, in bytes.
     | {CL_DRIVER_UUID_anchor}
     
- `api/opencl_platform_layer.asciidoc`:
     endif::cl_khr_device_uuid[]
     | {cl_uchar_TYPE}[{CL_UUID_SIZE}]
     
  >> ifdef::cl_khr_device_uuid[or {cl_uchar_TYPE}[{CL_UUID_SIZE_KHR}]]
     | Returns a universally unique identifier (UUID) for the software driver
     for the device.
     
- `api/opencl_platform_layer.asciidoc`:
     for the device.
     
     {CL_UUID_SIZE_anchor}
  >> ifdef::cl_khr_device_uuid[or {CL_UUID_SIZE_KHR_anchor}]
     is the size of the UUID, in bytes.
     | {CL_DEVICE_LUID_VALID_anchor}
     

## `CL_NAME_VERSION_MAX_NAME_SIZE_KHR`  (container: `Constants.cl_khr_extended_versioning`, value: 64)
- `api/cl_khr_extended_versioning.asciidoc`:
     === New Structures
     
     * {cl_name_version_khr_TYPE}
  >> * {CL_NAME_VERSION_MAX_NAME_SIZE_KHR_anchor}
     
     === New Macro Names
     

## `CL_VERSION_MAJOR_BITS_KHR`  (container: `Constants.cl_khr_extended_versioning`, value: 10)
- `api/cl_khr_extended_versioning.asciidoc`:
     
     === New Macro Names
     
  >> * {CL_VERSION_MAJOR_BITS_KHR_anchor}
     * {CL_VERSION_MINOR_BITS_KHR_anchor}
     * {CL_VERSION_PATCH_BITS_KHR_anchor}
     * {CL_VERSION_MAJOR_MASK_KHR_anchor}

## `CL_VERSION_MINOR_BITS_KHR`  (container: `Constants.cl_khr_extended_versioning`, value: 10)
- `api/cl_khr_extended_versioning.asciidoc`:
     === New Macro Names
     
     * {CL_VERSION_MAJOR_BITS_KHR_anchor}
  >> * {CL_VERSION_MINOR_BITS_KHR_anchor}
     * {CL_VERSION_PATCH_BITS_KHR_anchor}
     * {CL_VERSION_MAJOR_MASK_KHR_anchor}
     * {CL_VERSION_MINOR_MASK_KHR_anchor}

## `CL_VERSION_PATCH_BITS_KHR`  (container: `Constants.cl_khr_extended_versioning`, value: 12)
- `api/cl_khr_extended_versioning.asciidoc`:
     
     * {CL_VERSION_MAJOR_BITS_KHR_anchor}
     * {CL_VERSION_MINOR_BITS_KHR_anchor}
  >> * {CL_VERSION_PATCH_BITS_KHR_anchor}
     * {CL_VERSION_MAJOR_MASK_KHR_anchor}
     * {CL_VERSION_MINOR_MASK_KHR_anchor}
     * {CL_VERSION_PATCH_MASK_KHR_anchor}

## `CL_LAYER_API_VERSION_100`  (container: `Constants.cl_loader_layers`, value: 100)
- `extensions/cl_loader_layers.asciidoc`:
     
     [source,opencl]
     ----
  >> #define CL_LAYER_API_VERSION_100 100
     ----
     
     New in version 1.0.1, used to end the list of properties given to

## `CL_LAYER_PROPERTIES_LIST_END`  (container: `Constants.cl_loader_layers`, value: ((cl_layer_properties)0))
- `extensions/cl_loader_layers.asciidoc`:
     
     [source,opencl]
     ----
  >> #define CL_LAYER_PROPERTIES_LIST_END         ((cl_layer_properties)0)
     ----
     
     [[cl_loader_layers-new-environment-variables]]
- `extensions/cl_loader_layers.asciidoc`:
     * _properties_  specifies a list of layer property names and their
     corresponding values. Each property name is immediately followed by the
     corresponding desired value. The list is terminated with
  >> `CL_LAYER_PROPERTIES_LIST_END`. No properties are supported as of version
     1.0.1. _properties_ can be NULL, in which case all properties take on
     their default values.
     

## `CL_LUID_SIZE`  (container: `Constants.uuid`, value: 8)
- `api/opencl_platform_layer.asciidoc`:
     
     [version-note]
     endif::cl_khr_device_uuid[]
  >> | {cl_uchar_TYPE}[{CL_LUID_SIZE}]
     
     ifdef::cl_khr_device_uuid[or {cl_uchar_TYPE}[{CL_LUID_SIZE_KHR}]]
     | Returns a locally unique identifier (LUID) for the device.

## `CL_UUID_SIZE`  (container: `Constants.uuid`, value: 16)
- `api/opencl_platform_layer.asciidoc`:
     
     [version-note]
     endif::cl_khr_device_uuid[]
  >> | {cl_uchar_TYPE}[{CL_UUID_SIZE}]
     
     ifdef::cl_khr_device_uuid[or {cl_uchar_TYPE}[{CL_UUID_SIZE_KHR}]]
     | Returns a universally unique identifier (UUID) for the device.
- `api/opencl_platform_layer.asciidoc`:
     Device UUIDs must be immutable for a given device across processes,
     driver APIs, driver versions, and system reboots.
     
  >> {CL_UUID_SIZE_anchor}
     ifdef::cl_khr_device_uuid[or {CL_UUID_SIZE_KHR_anchor}]
     is the size of the UUID, in bytes.
     | {CL_DRIVER_UUID_anchor}
- `api/opencl_platform_layer.asciidoc`:
     
     [version-note]
     endif::cl_khr_device_uuid[]
  >> | {cl_uchar_TYPE}[{CL_UUID_SIZE}]
     
     ifdef::cl_khr_device_uuid[or {cl_uchar_TYPE}[{CL_UUID_SIZE_KHR}]]
     | Returns a universally unique identifier (UUID) for the software driver
- `api/opencl_platform_layer.asciidoc`:
     | Returns a universally unique identifier (UUID) for the software driver
     for the device.
     
  >> {CL_UUID_SIZE_anchor}
     ifdef::cl_khr_device_uuid[or {CL_UUID_SIZE_KHR_anchor}]
     is the size of the UUID, in bytes.
     | {CL_DEVICE_LUID_VALID_anchor}

## `CL_DEVICE_PARTITION_BY_COUNTS_LIST_END`  (container: `MiscNumbers`, value: 0x0)
- `api/opencl_platform_layer.asciidoc`:
     [version-note]
     | {cl_uint_TYPE}
     | This property is followed by a list of compute unit counts
  >> terminated with 0 or {CL_DEVICE_PARTITION_BY_COUNTS_LIST_END_anchor}.
     For each non-zero count _m_ in the list, a sub-device is created
     with _m_ compute units in it.
     
- `api/opencl_platform_layer.asciidoc`:
     [source,opencl]
     ----
     { CL_DEVICE_PARTITION_BY_COUNTS,
  >> 3, 1, CL_DEVICE_PARTITION_BY_COUNTS_LIST_END,
     0 } // 0 terminates the property list
     ----
     

## `CL_PARTITION_BY_COUNTS_LIST_END_EXT`  (container: `MiscNumbers`, value: ((cl_device_partition_property_ext)0))
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_PARTITION_BY_NAMES_LIST_END_EXT`  (container: `MiscNumbers`, value: ((cl_device_partition_property_ext)0 - 1))
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_PARTITION_BY_NAMES_LIST_END_INTEL`  (container: `MiscNumbers`, value: -1)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_PROPERTIES_LIST_END_EXT`  (container: `MiscNumbers`, value: ((cl_device_partition_property_ext)0))
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMPLETE`  (container: `clCommandExecutionStatus`, value: 0x0)
- `api/appendix_e.asciidoc`:
     * Added required support for sub-groups, see {CL_DEVICE_MAX_NUM_SUB_GROUPS}.
     * Relaxed the definition of inclusive scopes, see internal issue 367.
     * Clarified and un-deprecated the {CL_DEVICE_HOST_UNIFIED_MEMORY} query, see internal issue 370.
  >> * Updated the memory model so observing that an event is {CL_COMPLETE} is a synchronization point, see internal issue 373.
     * Allowed {clSetKernelArg} to set a local memory kernel argument to zero, see internal issue 374.
     * Deprecated the confusingly named {CL_DEVICE_MAX_WORK_ITEM_SIZES} query, use {CL_DEVICE_MAX_WORK_GROUP_SIZES} instead, see internal issue 375.
     * Cleaned up inconsistencies in the error condition descriptions for {clSetKernelExecInfo}, see {khronos-opencl-pr}/1419[#1419].
- `api/appendix_e.asciidoc`:
     
     Changes from *v3.1.0* to *v3.1.1*:
     
  >> * Reverted the change where observing that an event is {CL_COMPLETE} is a synchronization point due to possible performance regressions, see internal 
     
     Changes from *v3.1.1* to *v3.1.2*:
     
- `api/footnotes.asciidoc`:
     
     :fn-event-status-order: pass:n[ \
     The error code values are negative, and event state values are positive. \
  >> The event state values are ordered from the largest value {CL_QUEUED} for the first or initial state to the smallest value ({CL_COMPLETE} or negative 
     The value of {CL_COMPLETE} and {CL_SUCCESS} are the same. \
     ]
     
- `api/footnotes.asciidoc`:
     :fn-event-status-order: pass:n[ \
     The error code values are negative, and event state values are positive. \
     The event state values are ordered from the largest value {CL_QUEUED} for the first or initial state to the smallest value ({CL_COMPLETE} or negative 
  >> The value of {CL_COMPLETE} and {CL_SUCCESS} are the same. \
     ]
     
     :fn-get-device-ids-all-or-subset: pass:n[ \
- `api/opencl_architecture.asciidoc`:
     These side effects include updates to values in global memory.
     . *Complete*: The command and its child commands have finished execution
     and the status of the event object, if any, associated with the command
  >> is set to {CL_COMPLETE}.
     
     The <<profiled-states-image, execution states and the transitions between
     them>> are summarized below.
- `api/opencl_architecture.asciidoc`:
     
     Commands communicate their status through _event objects_.
     Successful completion is indicated by setting the event status associated
  >> with a command to {CL_COMPLETE}.
     Unsuccessful completion results in abnormal termination of the command which
     is indicated by setting the event status to a negative value.
     In this case, the command-queue associated with the abnormally terminated

## `CL_QUEUED`  (container: `clCommandExecutionStatus`, value: 0x3)
- `api/footnotes.asciidoc`:
     
     :fn-event-status-order: pass:n[ \
     The error code values are negative, and event state values are positive. \
  >> The event state values are ordered from the largest value {CL_QUEUED} for the first or initial state to the smallest value ({CL_COMPLETE} or negative 
     The value of {CL_COMPLETE} and {CL_SUCCESS} are the same. \
     ]
     
- `api/opencl_runtime_layer.asciidoc`:
     The execution status of an enqueued command at any given point in time can
     be one of the following:
     
  >> * {CL_QUEUED_anchor}: Indicates that the command has been enqueued in a
     command-queue.
     This is the initial state of all events except user events.
     * {CL_SUBMITTED_anchor}: The initial state for all user events.
- `api/opencl_runtime_layer.asciidoc`:
     | Return the execution status of the command identified by event.
     Valid values are:
     
  >> {CL_QUEUED} - Command has been enqueued in the command-queue.
     
     {CL_SUBMITTED} - Enqueued command has been submitted by the host to the
     device associated with the command-queue.
- `api/opencl_runtime_layer.asciidoc`:
     to multiple command-queues the semantics of execution status is as
     follows:
     
  >> {CL_QUEUED} - Command-buffer has been enqueued across the
     command-queues.
     
     {CL_SUBMITTED} - Commands from the command-buffer have been
- `extensions/cl_img_cancel_command.asciidoc`:
     const cl_event *event_list);
     ----
     is used to inform the OpenCL implementation that a list of commands that were previously enqueued are no longer required. +
  >> Any commands belonging to events in the _event_list_ that are in the `CL_QUEUED` state will not be executed. These events will be set to the `CL_CANCE
     Any commands belonging to events in the _event_list_ that are in the `CL_SUBMITTED` might not be executed. These events will be set to the `CL_CANCELL
     Any commands belonging to events in the _event_list_ that are in the `CL_RUNNING`, `CL_COMPLETE` or an error state will not be affected. +
     Any other command in the `CL_QUEUED` state that has a `CL_CANCELLED_IMG` event in its event_wait_list will not be executed. The events belonging to th
- `extensions/cl_img_cancel_command.asciidoc`:
     Any commands belonging to events in the _event_list_ that are in the `CL_QUEUED` state will not be executed. These events will be set to the `CL_CANCE
     Any commands belonging to events in the _event_list_ that are in the `CL_SUBMITTED` might not be executed. These events will be set to the `CL_CANCELL
     Any commands belonging to events in the _event_list_ that are in the `CL_RUNNING`, `CL_COMPLETE` or an error state will not be affected. +
  >> Any other command in the `CL_QUEUED` state that has a `CL_CANCELLED_IMG` event in its event_wait_list will not be executed. The events belonging to th
     
     _event_list_ and _num_events_in_list_ specify events that belong to commands that no longer need to be executed.
     If _event_list_ is `NULL`, _num_events_in_list_ must be 0.

## `CL_RUNNING`  (container: `clCommandExecutionStatus`, value: 0x1)
- `api/opencl_runtime_layer.asciidoc`:
     * {CL_SUBMITTED_anchor}: The initial state for all user events.
     For all other events, indicates that the command has been submitted
     by the host to the device.
  >> * {CL_RUNNING_anchor}: Indicates that the device has started executing this
     command.
     In order for the execution status of an enqueued command to change from
     {CL_SUBMITTED} to {CL_RUNNING}, all events that this command is waiting on
- `api/opencl_runtime_layer.asciidoc`:
     * {CL_RUNNING_anchor}: Indicates that the device has started executing this
     command.
     In order for the execution status of an enqueued command to change from
  >> {CL_SUBMITTED} to {CL_RUNNING}, all events that this command is waiting on
     must have completed successfully i.e. their execution status must be
     {CL_COMPLETE}.
     * {CL_COMPLETE_anchor}: Indicates that the command has successfully completed.
- `api/opencl_runtime_layer.asciidoc`:
     {CL_SUBMITTED} - Enqueued command has been submitted by the host to the
     device associated with the command-queue.
     
  >> {CL_RUNNING} - Device is currently executing this command.
     
     {CL_COMPLETE} - The command has completed.
     
- `api/opencl_runtime_layer.asciidoc`:
     submitted by the host to any device associated with one of the
     command-queues.
     
  >> {CL_RUNNING} - Any command from the command-buffer has started
     execution on a device.
     
     {CL_COMPLETE} - All commands have completed on all devices.
- `api/opencl_runtime_layer.asciidoc`:
     * _command_exec_callback_type_ specifies the command execution status for
     which the callback is registered.
     The command execution status types for which a callback can be registered
  >> are {CL_SUBMITTED}, {CL_RUNNING}, or {CL_COMPLETE}.
     The callback function registered for a _command_exec_callback_type_ value of
     {CL_COMPLETE} will be called when the command has completed successfully or
     is abnormally terminated.
- `api/opencl_runtime_layer.asciidoc`:
     
     * {CL_INVALID_EVENT} if _event_ is not a valid event object.
     * {CL_INVALID_VALUE} if _pfn_event_notify_ is `NULL` or if
  >> _command_exec_callback_type_ is not {CL_SUBMITTED}, {CL_RUNNING}, or
     {CL_COMPLETE}.
     * {CL_OUT_OF_RESOURCES} if there is a failure to allocate resources required
     by the OpenCL implementation on the device.

## `CL_SUBMITTED`  (container: `clCommandExecutionStatus`, value: 0x2)
- `api/opencl_runtime_layer.asciidoc`:
     * {CL_QUEUED_anchor}: Indicates that the command has been enqueued in a
     command-queue.
     This is the initial state of all events except user events.
  >> * {CL_SUBMITTED_anchor}: The initial state for all user events.
     For all other events, indicates that the command has been submitted
     by the host to the device.
     * {CL_RUNNING_anchor}: Indicates that the device has started executing this
- `api/opencl_runtime_layer.asciidoc`:
     * {CL_RUNNING_anchor}: Indicates that the device has started executing this
     command.
     In order for the execution status of an enqueued command to change from
  >> {CL_SUBMITTED} to {CL_RUNNING}, all events that this command is waiting on
     must have completed successfully i.e. their execution status must be
     {CL_COMPLETE}.
     * {CL_COMPLETE_anchor}: Indicates that the command has successfully completed.
- `api/opencl_runtime_layer.asciidoc`:
     * {CL_OUT_OF_HOST_MEMORY} if there is a failure to allocate resources
     required by the OpenCL implementation on the host.
     
  >> The initial execution status for the user event object is {CL_SUBMITTED}.
     --
     
     [open,refpage='clSetUserEventStatus',desc='Sets the execution status of a user event object.',type='protos']
- `api/opencl_runtime_layer.asciidoc`:
     
     {CL_QUEUED} - Command has been enqueued in the command-queue.
     
  >> {CL_SUBMITTED} - Enqueued command has been submitted by the host to the
     device associated with the command-queue.
     
     {CL_RUNNING} - Device is currently executing this command.
- `api/opencl_runtime_layer.asciidoc`:
     {CL_QUEUED} - Command-buffer has been enqueued across the
     command-queues.
     
  >> {CL_SUBMITTED} - Commands from the command-buffer have been
     submitted by the host to any device associated with one of the
     command-queues.
     
- `api/opencl_runtime_layer.asciidoc`:
     * _command_exec_callback_type_ specifies the command execution status for
     which the callback is registered.
     The command execution status types for which a callback can be registered
  >> are {CL_SUBMITTED}, {CL_RUNNING}, or {CL_COMPLETE}.
     The callback function registered for a _command_exec_callback_type_ value of
     {CL_COMPLETE} will be called when the command has completed successfully or
     is abnormally terminated.

## `CL_ADDRESS_CLAMP`  (container: `cl_device_info`, value: 0x1132)
- `api/opencl_runtime_layer.asciidoc`:
     {CL_ADDRESS_CLAMP_TO_EDGE_anchor} - Out-of-range image coordinates
     are clamped to the edge of the image.
     
  >> {CL_ADDRESS_CLAMP_anchor} - Out-of-range image coordinates are
     assigned a border color value.
     
     {CL_ADDRESS_REPEAT_anchor} - Out-of-range image coordinates read
- `api/opencl_runtime_layer.asciidoc`:
     dimensions, mirroring the image contents at the edge of each
     replication.
     
  >> The default is {CL_ADDRESS_CLAMP}.
     | {CL_SAMPLER_FILTER_MODE_anchor}
     
     [version-note]
- `env/image_addressing_and_filtering.asciidoc`:
     [[clamp-addressing]]
     ==== Clamp and None Addressing Modes
     
  >> We first describe how the addressing and filter modes are applied to generate the appropriate sample locations to read from the image if the addressin
     
     [[clamp-nearest_filtering]]
     ===== Nearest Filtering
- `env/image_addressing_and_filtering.asciidoc`:
     a|*Addressing Mode*
     a|*Result of _address_mode(coord)_*
     
  >> a|{CL_ADDRESS_CLAMP}
     a|_clamp (coord, -1, size)_
     
     a|{CL_ADDRESS_CLAMP_TO_EDGE}
- `env/image_addressing_and_filtering.asciidoc`:
     \end{aligned}
     ++++
     
  >> If the addressing mode is {CL_ADDRESS_CLAMP} or {CL_ADDRESS_CLAMP_TO_EDGE}, and the selected texel location `(i,j,k)` refers to a location outside the
     
     Otherwise, if the addressing mode is {CL_ADDRESS_NONE} and the selected texel location `(i,j,k)` refers to a location outside the image, the color val
     
- `env/image_addressing_and_filtering.asciidoc`:
     
     where `T~ij~` is the image element at location `(i,j)` in the 2D image.
     
  >> If the addressing mode is {CL_ADDRESS_CLAMP} or {CL_ADDRESS_CLAMP_TO_EDGE}, and any of the selected `T~ijk~` or `T~ij~` refers to a location outside t
     
     Otherwise, if the addressing mode is {CL_ADDRESS_NONE}, and any of the selected `T~ijk~` or `T~ij~` refers to a location outside the image, the color 
     

## `CL_ADDRESS_CLAMP_TO_EDGE`  (container: `cl_device_info`, value: 0x1131)
- `api/opencl_runtime_layer.asciidoc`:
     {CL_ADDRESS_NONE_anchor} - Behavior is undefined for out-of-range
     image coordinates.
     
  >> {CL_ADDRESS_CLAMP_TO_EDGE_anchor} - Out-of-range image coordinates
     are clamped to the edge of the image.
     
     {CL_ADDRESS_CLAMP_anchor} - Out-of-range image coordinates are
- `env/image_addressing_and_filtering.asciidoc`:
     [[clamp-addressing]]
     ==== Clamp and None Addressing Modes
     
  >> We first describe how the addressing and filter modes are applied to generate the appropriate sample locations to read from the image if the addressin
     
     [[clamp-nearest_filtering]]
     ===== Nearest Filtering
- `env/image_addressing_and_filtering.asciidoc`:
     a|{CL_ADDRESS_CLAMP}
     a|_clamp (coord, -1, size)_
     
  >> a|{CL_ADDRESS_CLAMP_TO_EDGE}
     a|_clamp (coord, 0, size - 1)_
     
     a|{CL_ADDRESS_NONE}
- `env/image_addressing_and_filtering.asciidoc`:
     \end{aligned}
     ++++
     
  >> If the addressing mode is {CL_ADDRESS_CLAMP} or {CL_ADDRESS_CLAMP_TO_EDGE}, and the selected texel location `(i,j,k)` refers to a location outside the
     
     Otherwise, if the addressing mode is {CL_ADDRESS_NONE} and the selected texel location `(i,j,k)` refers to a location outside the image, the color val
     
- `env/image_addressing_and_filtering.asciidoc`:
     
     where `T~ij~` is the image element at location `(i,j)` in the 2D image.
     
  >> If the addressing mode is {CL_ADDRESS_CLAMP} or {CL_ADDRESS_CLAMP_TO_EDGE}, and any of the selected `T~ijk~` or `T~ij~` refers to a location outside t
     
     Otherwise, if the addressing mode is {CL_ADDRESS_NONE}, and any of the selected `T~ijk~` or `T~ij~` refers to a location outside the image, the color 
     
- `env/image_addressing_and_filtering.asciidoc`:
     [[precision-of-addressing-and-filter-modes]]
     === Precision of Addressing and Filter Modes
     
  >> If the sampler is specified as using unnormalized coordinates (floating-point or integer coordinates), filter mode set to {CL_FILTER_NEAREST} and addr
     
     For all other sampler combinations of normalized or unnormalized coordinates, filter modes, and addressing modes, the relative error or precision of t
     To ensure precision of image addressing and filter calculations across any OpenCL device for these sampler combinations, developers may unnormalize th

## `CL_ADDRESS_MIRRORED_REPEAT`  (container: `cl_device_info`, value: 0x1134)
- `api/opencl_runtime_layer.asciidoc`:
     {CL_ADDRESS_REPEAT_anchor} - Out-of-range image coordinates read
     from the image as if the image data were replicated in all dimensions.
     
  >> {CL_ADDRESS_MIRRORED_REPEAT_anchor} - Out-of-range image coordinates
     read from the image as if the image data were replicated in all
     dimensions, mirroring the image contents at the edge of each
     replication.
- `env/image_addressing_and_filtering.asciidoc`:
     [[mirrored-repeat-addressing]]
     ==== Mirrored Repeat Addressing Mode
     
  >> We now discuss how the addressing and filter modes are applied to generate the appropriate sample locations to read from the image if the addressing m
     The {CL_ADDRESS_MIRRORED_REPEAT} addressing mode causes the image to be read as if it is tiled at every integer seam, with the interpretation of the i
     
     [[mirrored-repeat-nearest-filtering]]
- `env/image_addressing_and_filtering.asciidoc`:
     ==== Mirrored Repeat Addressing Mode
     
     We now discuss how the addressing and filter modes are applied to generate the appropriate sample locations to read from the image if the addressing m
  >> The {CL_ADDRESS_MIRRORED_REPEAT} addressing mode causes the image to be read as if it is tiled at every integer seam, with the interpretation of the i
     
     [[mirrored-repeat-nearest-filtering]]
     ===== Nearest Filtering

## `CL_ADDRESS_NONE`  (container: `cl_device_info`, value: 0x1130)
- `api/opencl_runtime_layer.asciidoc`:
     reading from an image.
     Valid values are:
     
  >> {CL_ADDRESS_NONE_anchor} - Behavior is undefined for out-of-range
     image coordinates.
     
     {CL_ADDRESS_CLAMP_TO_EDGE_anchor} - Out-of-range image coordinates
- `env/image_addressing_and_filtering.asciidoc`:
     [[clamp-addressing]]
     ==== Clamp and None Addressing Modes
     
  >> We first describe how the addressing and filter modes are applied to generate the appropriate sample locations to read from the image if the addressin
     
     [[clamp-nearest_filtering]]
     ===== Nearest Filtering
- `env/image_addressing_and_filtering.asciidoc`:
     a|{CL_ADDRESS_CLAMP_TO_EDGE}
     a|_clamp (coord, 0, size - 1)_
     
  >> a|{CL_ADDRESS_NONE}
     a|_coord_
     |====
     
- `env/image_addressing_and_filtering.asciidoc`:
     
     If the addressing mode is {CL_ADDRESS_CLAMP} or {CL_ADDRESS_CLAMP_TO_EDGE}, and the selected texel location `(i,j,k)` refers to a location outside the
     
  >> Otherwise, if the addressing mode is {CL_ADDRESS_NONE} and the selected texel location `(i,j,k)` refers to a location outside the image, the color val
     
     [[clamp-linear-filtering]]
     ===== Linear Filtering
- `env/image_addressing_and_filtering.asciidoc`:
     
     If the addressing mode is {CL_ADDRESS_CLAMP} or {CL_ADDRESS_CLAMP_TO_EDGE}, and any of the selected `T~ijk~` or `T~ij~` refers to a location outside t
     
  >> Otherwise, if the addressing mode is {CL_ADDRESS_NONE}, and any of the selected `T~ijk~` or `T~ij~` refers to a location outside the image, the color 
     
     If the image channel type is {CL_FLOAT} or {CL_HALF_FLOAT}, and any of the image elements `T~ijk~` or `T~ij~` is INF or NaN, the color value is undefi
     
- `env/image_addressing_and_filtering.asciidoc`:
     [[precision-of-addressing-and-filter-modes]]
     === Precision of Addressing and Filter Modes
     
  >> If the sampler is specified as using unnormalized coordinates (floating-point or integer coordinates), filter mode set to {CL_FILTER_NEAREST} and addr
     
     For all other sampler combinations of normalized or unnormalized coordinates, filter modes, and addressing modes, the relative error or precision of t
     To ensure precision of image addressing and filter calculations across any OpenCL device for these sampler combinations, developers may unnormalize th

## `CL_ADDRESS_REPEAT`  (container: `cl_device_info`, value: 0x1133)
- `api/opencl_runtime_layer.asciidoc`:
     {CL_ADDRESS_CLAMP_anchor} - Out-of-range image coordinates are
     assigned a border color value.
     
  >> {CL_ADDRESS_REPEAT_anchor} - Out-of-range image coordinates read
     from the image as if the image data were replicated in all dimensions.
     
     {CL_ADDRESS_MIRRORED_REPEAT_anchor} - Out-of-range image coordinates
- `env/image_addressing_and_filtering.asciidoc`:
     [[repeat-addressing]]
     ==== Repeat Addressing Mode
     
  >> We now discuss how the addressing and filter modes are applied to generate the appropriate sample locations to read from the image if the addressing m
     
     [[repeat-nearest-filtering]]
     ===== Nearest Filtering

## `CL_COMMAND_SVM_MIGRATE_MEM`  (container: `cl_device_info`, value: 0x120E)
- `api/appendix_e.asciidoc`:
     OpenCL 3.0 adds an event command type to identify events
     associated with the OpenCL 2.1 command {clEnqueueSVMMigrateMem}:
     
  >> * {CL_COMMAND_SVM_MIGRATE_MEM}
     
     OpenCL 3.0 adds a new query to determine the latest version of the conformance
     test suite that the device has fully passed in accordance with the official
- `api/opencl_runtime_layer.asciidoc`:
     [version-note]
     
     | {clEnqueueSVMMigrateMem}
  >> | {CL_COMMAND_SVM_MIGRATE_MEM_anchor}
     
     [version-note]
     
- `api/opencl_runtime_layer.asciidoc`:
     | {clEnqueueSVMMigrateMem}
     | {CL_COMMAND_SVM_MIGRATE_MEM_anchor}
     
  >> [version-note]
     
     Prior to OpenCL 3.0, implementations should return
     {CL_COMMAND_MIGRATE_MEM_OBJECTS}, but may return an implementation-defined

## `CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION`  (container: `cl_device_info`, value: 0x1062)
- `api/appendix_e.asciidoc`:
     device extensions and their supported version.
     * {CL_DEVICE_ILS_WITH_VERSION} to describe supported
     intermediate languages (ILs) and their supported version.
  >> * {CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION} to describe supported
     built-in kernels and their supported version.
     
     OpenCL 3.0 adds a new API to register a function that will be called
- `api/opencl_platform_layer.asciidoc`:
     An empty string is returned if no built-in kernels are supported by
     the device.
     
  >> | {CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_extended_versioning[]
     or

## `CL_DEVICE_EXTENSIONS_WITH_VERSION`  (container: `cl_device_info`, value: 0x1060)
- `api/appendix_e.asciidoc`:
     platform extensions and their supported version.
     * {CL_DEVICE_NUMERIC_VERSION} to describe the device version
     as a numeric value.
  >> * {CL_DEVICE_EXTENSIONS_WITH_VERSION} to describe supported
     device extensions and their supported version.
     * {CL_DEVICE_ILS_WITH_VERSION} to describe supported
     intermediate languages (ILs) and their supported version.
- `api/opencl_platform_layer.asciidoc`:
     Please refer to the OpenCL Specification or vendor-provided
     documentation for a detailed description of these extensions.
     
  >> | {CL_DEVICE_EXTENSIONS_WITH_VERSION_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_EXTENSIONS_WITH_VERSION_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_extended_versioning[]
     or
- `api/opencl_platform_layer.asciidoc`:
     Some OpenCL features were originally OpenCL extensions before adoption into the
     core OpenCL standard.
     This section describes the OpenCL extensions that must be reported by a device
  >> through {CL_DEVICE_EXTENSIONS} or {CL_DEVICE_EXTENSIONS_WITH_VERSION} for the
     OpenCL version reported by {CL_DEVICE_VERSION}.
     
     The following Khronos extension names must be returned by all devices that

## `CL_DEVICE_ILS_WITH_VERSION`  (container: `cl_device_info`, value: 0x1061)
- `api/appendix_e.asciidoc`:
     as a numeric value.
     * {CL_DEVICE_EXTENSIONS_WITH_VERSION} to describe supported
     device extensions and their supported version.
  >> * {CL_DEVICE_ILS_WITH_VERSION} to describe supported
     intermediate languages (ILs) and their supported version.
     * {CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION} to describe supported
     built-in kernels and their supported version.
- `api/appendix_h.asciidoc`:
     
     | {clGetDeviceInfo}, passing +
     {CL_DEVICE_IL_VERSION} or +
  >> {CL_DEVICE_ILS_WITH_VERSION}
     | May return an empty string and empty array, indicating that _device_ does not support intermediate language programs.
     
     | {clGetProgramInfo}, passing +
- `api/opencl_assoc_spec.asciidoc`:
     The OpenCL specifications include the SPIR-V specification, which defines a
     cross-platform intermediate language.
     When an OpenCL device supports one or more versions of SPIR-V (see
  >> {CL_DEVICE_IL_VERSION} or {CL_DEVICE_ILS_WITH_VERSION}), OpenCL program objects
     may be created by passing SPIR-V to {clCreateProgramWithIL}.
     
     
- `api/opencl_platform_layer.asciidoc`:
     If the device does not support intermediate language programs, the
     returned value must be `""` (an empty string).
     
  >> | {CL_DEVICE_ILS_WITH_VERSION_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_ILS_WITH_VERSION_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_extended_versioning[]
     or
- `env/common_properties.asciidoc`:
     
     An OpenCL device describes the versions of SPIR-V modules that it
     supports using the {CL_DEVICE_IL_VERSION} query in OpenCL 2.1 or newer,
  >> the {CL_DEVICE_ILS_WITH_VERSION} query in OpenCL 3.0 or newer, or the
     {CL_DEVICE_IL_VERSION_KHR} query in the {cl_khr_il_program_EXT} extension.
     
     OpenCL devices that support the {cl_khr_il_program_EXT} extension or

## `CL_DEVICE_IL_VERSION`  (container: `cl_device_info`, value: 0x105B)
- `api/appendix_e.asciidoc`:
     * {clSetDefaultDeviceCommandQueue} API call.
     * {CL_PLATFORM_HOST_TIMER_RESOLUTION} added to table 4.1 of the API
     specification.
  >> * {CL_DEVICE_IL_VERSION}, {CL_DEVICE_MAX_NUM_SUB_GROUPS},
     {CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS} added to table 4.3 of
     the API specification.
     * {CL_PROGRAM_IL} to table 5.17 of the API specification.
- `api/appendix_h.asciidoc`:
     |*Behavior*
     
     | {clGetDeviceInfo}, passing +
  >> {CL_DEVICE_IL_VERSION} or +
     {CL_DEVICE_ILS_WITH_VERSION}
     | May return an empty string and empty array, indicating that _device_ does not support intermediate language programs.
     
- `api/opencl_assoc_spec.asciidoc`:
     The OpenCL specifications include the SPIR-V specification, which defines a
     cross-platform intermediate language.
     When an OpenCL device supports one or more versions of SPIR-V (see
  >> {CL_DEVICE_IL_VERSION} or {CL_DEVICE_ILS_WITH_VERSION}), OpenCL program objects
     may be created by passing SPIR-V to {clCreateProgramWithIL}.
     
     
- `api/opencl_platform_layer.asciidoc`:
     
     The minimum value is 64 if the device supports read-write images arguments,
     and must be 0 for devices that do not support read-write images.
  >> | {CL_DEVICE_IL_VERSION_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     and must be 0 for devices that do not support read-write images.
     | {CL_DEVICE_IL_VERSION_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_il_program[]
     or
- `api/opencl_platform_layer.asciidoc`:
     once but each name and major/minor version combination may only be
     reported once.
     The list of intermediate languages reported must match the list
  >> reported via {CL_DEVICE_IL_VERSION}.
     
     | {CL_DEVICE_IMAGE2D_MAX_WIDTH_anchor}
     

## `CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT`  (container: `cl_device_info`, value: 0x104B)
- `api/appendix_c.asciidoc`:
     This implies that OpenCL images created with {CL_MEM_USE_HOST_PTR} must align
     correctly.
     The image alignment value can be queried using the
  >> {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT} query.
     In addition, source pointers for {clEnqueueWriteImage} and other operations
     that copy to the OpenCL runtime, as well as destination pointers for
     {clEnqueueReadImage} and other operations that copy from the OpenCL runtime
- `api/appendix_h.asciidoc`:
     
     | {clGetDeviceInfo}, passing +
     {CL_DEVICE_IMAGE_PITCH_ALIGNMENT} or +
  >> {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT}
     | May return `0`, indicating that _device_ does not support creating a 2D image from a Buffer.
     
     | {clGetDeviceInfo}, passing +
- `api/cl_ext_image_requirements_info.asciidoc`:
     
     . Check consistency with `cl_khr_image2d_from_buffer`
     * When `cl_khr_image2d_from_buffer` is supported, check that the value returned by {CL_DEVICE_IMAGE_PITCH_ALIGNMENT} after converting in bytes for the
  >> * When `cl_khr_image2d_from_buffer` is supported, check that the value returned by {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT} after converting in bytes 
     
     . Negative tests for {CL_IMAGE_REQUIREMENTS_SIZE_EXT}
     * Check that attempting to perform the {CL_IMAGE_REQUIREMENTS_SIZE_EXT} query without specifying the _image_format_ results in {CL_INVALID_VALUE} bein
- `api/opencl_platform_layer.asciidoc`:
     supported format.
     endif::cl_ext_image_requirements_info+cl_khr_image2d_from_buffer[]
     
  >> | {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_image2d_from_buffer[]
     The equivalent {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT_KHR_anchor} may be used
- `api/opencl_platform_layer.asciidoc`:
     ifdef::cl_ext_image_requirements_info+cl_khr_image2d_from_buffer[]
     If the {cl_khr_image2d_from_buffer_EXT} and {cl_ext_image_requirements_info_EXT}
     extensions are supported, the value returned by
  >> {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT} after converting in bytes for the
     supported format with the biggest element size
     (channel data type size {times} number of channels) must be greater than or equal to
     the value returned by {CL_IMAGE_REQUIREMENTS_BASE_ADDRESS_ALIGNMENT_EXT} for any

## `CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT_KHR`  (container: `cl_device_info`, value: 0x104B)
- `api/cl_khr_image2d_from_buffer.asciidoc`:
     === New Enums
     
     * {CL_DEVICE_IMAGE_PITCH_ALIGNMENT_KHR}
  >> * {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT_KHR}
     
     === Version History
     
- `api/opencl_platform_layer.asciidoc`:
     [version-note]
     
     ifdef::cl_khr_image2d_from_buffer[]
  >> The equivalent {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT_KHR_anchor} may be used
     if the {cl_khr_image2d_from_buffer_EXT} extension is supported.
     endif::cl_khr_image2d_from_buffer[]
     | {cl_uint_TYPE}

## `CL_DEVICE_IMAGE_PITCH_ALIGNMENT`  (container: `cl_device_info`, value: 0x104A)
- `api/appendix_h.asciidoc`:
     |*Behavior*
     
     | {clGetDeviceInfo}, passing +
  >> {CL_DEVICE_IMAGE_PITCH_ALIGNMENT} or +
     {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT}
     | May return `0`, indicating that _device_ does not support creating a 2D image from a Buffer.
     
- `api/cl_ext_image_requirements_info.asciidoc`:
     ** Check that the {CL_IMAGE_REQUIREMENTS_BASE_ADDRESS_ALIGNMENT_EXT} and {CL_IMAGE_REQUIREMENTS_ROW_PITCH_ALIGNMENT_EXT} queries can be performed succ
     
     . Check consistency with `cl_khr_image2d_from_buffer`
  >> * When `cl_khr_image2d_from_buffer` is supported, check that the value returned by {CL_DEVICE_IMAGE_PITCH_ALIGNMENT} after converting in bytes for the
     * When `cl_khr_image2d_from_buffer` is supported, check that the value returned by {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT} after converting in bytes 
     
     . Negative tests for {CL_IMAGE_REQUIREMENTS_SIZE_EXT}
- `api/opencl_platform_layer.asciidoc`:
     
     The minimum value is 16 if {CL_DEVICE_IMAGE_SUPPORT} is {CL_TRUE},
     the value is 0 otherwise.
  >> | {CL_DEVICE_IMAGE_PITCH_ALIGNMENT_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     the value is 0 otherwise.
     | {CL_DEVICE_IMAGE_PITCH_ALIGNMENT_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_image2d_from_buffer[]
     The equivalent {CL_DEVICE_IMAGE_PITCH_ALIGNMENT_KHR_anchor} may be used if
- `api/opencl_platform_layer.asciidoc`:
     
     ifdef::cl_ext_image_requirements_info+cl_khr_image2d_from_buffer[]
     If the {cl_khr_image2d_from_buffer_EXT} and {cl_ext_image_requirements_info_EXT}
  >> extensions are supported, the value returned by {CL_DEVICE_IMAGE_PITCH_ALIGNMENT}
     after converting in bytes for the supported format with the biggest element size
     (channel data type size {times} number of channels) must be greater than or equal to
     the value returned by {CL_IMAGE_REQUIREMENTS_ROW_PITCH_ALIGNMENT_EXT} for any
- `api/opencl_runtime_layer.asciidoc`:
     multiple of the size of an image element in bytes. +
     ifndef::cl_ext_image_requirements_info[]
     For a 2D image created from a buffer the _image_row_pitch_ must also be a
  >> multiple of the maximum of the {CL_DEVICE_IMAGE_PITCH_ALIGNMENT} value
     for all devices in the context that support images.
     endif::cl_ext_image_requirements_info[]
     ifdef::cl_ext_image_requirements_info[]

## `CL_DEVICE_IMAGE_PITCH_ALIGNMENT_KHR`  (container: `cl_device_info`, value: 0x104A)
- `api/cl_khr_image2d_from_buffer.asciidoc`:
     
     === New Enums
     
  >> * {CL_DEVICE_IMAGE_PITCH_ALIGNMENT_KHR}
     * {CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT_KHR}
     
     === Version History
- `api/opencl_platform_layer.asciidoc`:
     [version-note]
     
     ifdef::cl_khr_image2d_from_buffer[]
  >> The equivalent {CL_DEVICE_IMAGE_PITCH_ALIGNMENT_KHR_anchor} may be used if
     the {cl_khr_image2d_from_buffer_EXT} extension is supported.
     endif::cl_khr_image2d_from_buffer[]
     | {cl_uint_TYPE}

## `CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED`  (container: `cl_device_info`, value: 0x1075)
- `api/opencl_platform_layer.asciidoc`:
     extension.
     endif::cl_khr_integer_dot_product[]
     
  >> | {CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_integer_dot_product[]
     or

## `CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED_KHR`  (container: `cl_device_info`, value: 0x1075)
- `api/cl_khr_integer_dot_product.asciidoc`:
     * {cl_device_info_TYPE}
     ** {CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES_KHR}
     ** {CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_8BIT_KHR}
  >> ** {CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED_KHR}
     
     === Version History
     
- `api/opencl_platform_layer.asciidoc`:
     ifdef::cl_khr_integer_dot_product[]
     or
     
  >> {CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED_KHR_anchor}
     
     [version-note]
     endif::cl_khr_integer_dot_product[]
- `api/opencl_platform_layer.asciidoc`:
     
     {CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED_KHR_anchor}
     
  >> [version-note]
     endif::cl_khr_integer_dot_product[]
     | {cl_device_integer_dot_product_acceleration_properties_TYPE}
     
- `api/opencl_platform_layer.asciidoc`:
     accelerated, {CL_FALSE} otherwise.
     
     ifdef::cl_khr_integer_dot_product[]
  >> {CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED_KHR} is
     missing before version 2.0 of the {cl_khr_integer_dot_product_EXT}
     extension.
     endif::cl_khr_integer_dot_product[]

## `CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_8BIT`  (container: `cl_device_info`, value: 0x1074)
- `api/opencl_platform_layer.asciidoc`:
     is supported.
     endif::cl_khr_integer_dot_product[]
     
  >> | {CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_8BIT_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_8BIT_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_integer_dot_product[]
     or

## `CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES`  (container: `cl_device_info`, value: 0x1073)
- `api/opencl_platform_layer.asciidoc`:
     the Direct3D 12 node corresponding to the OpenCL device.
     Otherwise, the returned node mask must be `1`.
     
  >> | {CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_integer_dot_product[]
     or
- `api/opencl_platform_layer.asciidoc`:
     
     OpenCL 3.0 or newer devices must report the following feature macros via
     {CL_DEVICE_OPENCL_C_FEATURES} when the corresponding bit is set in the bitfield
  >> returned for {CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES}
     ifdef::cl_khr_integer_dot_product[or {CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES_KHR}:]
     ifndef::cl_khr_integer_dot_product[:]
     

## `CL_DEVICE_LUID`  (container: `cl_device_info`, value: 0x106D)
- `api/opencl_platform_layer.asciidoc`:
     | {cl_bool_TYPE}
     | Returns {CL_TRUE} if the device has a valid LUID and {CL_FALSE}
     otherwise.
  >> | {CL_DEVICE_LUID_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     otherwise.
     | {CL_DEVICE_LUID_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_device_uuid[]
     or
- `api/opencl_platform_layer.asciidoc`:
     ifdef::cl_khr_device_uuid[or {cl_uchar_TYPE}[{CL_LUID_SIZE_KHR}]]
     | Returns a locally unique identifier (LUID) for the device.
     
  >> It is not an error to query {CL_DEVICE_LUID}
     ifdef::cl_khr_device_uuid[or {CL_DEVICE_LUID_KHR}]
     when {CL_DEVICE_LUID_VALID}
     ifdef::cl_khr_device_uuid[or {CL_DEVICE_LUID_VALID_KHR}]

## `CL_DEVICE_LUID_VALID`  (container: `cl_device_info`, value: 0x106C)
- `api/opencl_platform_layer.asciidoc`:
     {CL_UUID_SIZE_anchor}
     ifdef::cl_khr_device_uuid[or {CL_UUID_SIZE_KHR_anchor}]
     is the size of the UUID, in bytes.
  >> | {CL_DEVICE_LUID_VALID_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     is the size of the UUID, in bytes.
     | {CL_DEVICE_LUID_VALID_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_device_uuid[]
     or
- `api/opencl_platform_layer.asciidoc`:
     
     It is not an error to query {CL_DEVICE_LUID}
     ifdef::cl_khr_device_uuid[or {CL_DEVICE_LUID_KHR}]
  >> when {CL_DEVICE_LUID_VALID}
     ifdef::cl_khr_device_uuid[or {CL_DEVICE_LUID_VALID_KHR}]
     returns {CL_FALSE}, but in this case the returned LUID value is
     undefined.
- `api/opencl_platform_layer.asciidoc`:
     
     It is not an error to query {CL_DEVICE_NODE_MASK}
     ifdef::cl_khr_device_uuid[or {CL_DEVICE_NODE_MASK_KHR}]
  >> when {CL_DEVICE_LUID_VALID}
     ifdef::cl_khr_device_uuid[or {CL_DEVICE_LUID_VALID_KHR}]
     returns {CL_FALSE}, but in this case the returned node mask is
     undefined.

## `CL_DEVICE_MAX_NUM_SUB_GROUPS`  (container: `cl_device_info`, value: 0x105C)
- `api/appendix_e.asciidoc`:
     * {clSetDefaultDeviceCommandQueue} API call.
     * {CL_PLATFORM_HOST_TIMER_RESOLUTION} added to table 4.1 of the API
     specification.
  >> * {CL_DEVICE_IL_VERSION}, {CL_DEVICE_MAX_NUM_SUB_GROUPS},
     {CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS} added to table 4.3 of
     the API specification.
     * {CL_PROGRAM_IL} to table 5.17 of the API specification.
- `api/appendix_e.asciidoc`:
     
     Other changes in OpenCL 3.1:
     
  >> * Added required support for sub-groups, see {CL_DEVICE_MAX_NUM_SUB_GROUPS}.
     * Relaxed the definition of inclusive scopes, see internal issue 367.
     * Clarified and un-deprecated the {CL_DEVICE_HOST_UNIFIED_MEMORY} query, see internal issue 370.
     * Updated the memory model so observing that an event is {CL_COMPLETE} is a synchronization point, see internal issue 373.
- `api/appendix_h.asciidoc`:
     |*Behavior*
     
     | {clGetDeviceInfo}, passing +
  >> {CL_DEVICE_MAX_NUM_SUB_GROUPS}
     | May return `0`, indicating that _device_ does not support sub-groups.
     
     | {clGetDeviceInfo}, passing +
- `api/opencl_platform_layer.asciidoc`:
     OpenCL 2.0 atomic types to local memory.
     This query can return 0 which indicates that the preferred alignment
     is aligned to the natural size of the type.
  >> | {CL_DEVICE_MAX_NUM_SUB_GROUPS_anchor}
     
     // Note: This sub-group property is not in cl_khr_subgroups.
     [version-note]
- `api/opencl_platform_layer.asciidoc`:
     | {CL_DEVICE_MAX_NUM_SUB_GROUPS_anchor}
     
     // Note: This sub-group property is not in cl_khr_subgroups.
  >> [version-note]
     | {cl_uint_TYPE}
     | Maximum number of sub-groups in a work-group that a device is
     capable of executing on a single compute unit, for any given
- `env/required_capabilities.asciidoc`:
     * *GenericPointer*
     ** For OpenCL 2.0, OpenCL 2.1, OpenCL 2.2, or OpenCL 3.0 devices supporting the Generic Address Space (where {CL_DEVICE_GENERIC_ADDRESS_SPACE_SUPPORT}
     * *Groups*
  >> ** For OpenCL 2.0, OpenCL 2.1, OpenCL 2.2, or OpenCL 3.0 devices supporting Sub-groups (where {CL_DEVICE_MAX_NUM_SUB_GROUPS} is not `0`) or Work-group
     * *Pipes*
     ** For OpenCL 2.0, OpenCL 2.1, OpenCL 2.2, or OpenCL 3.0 devices supporting Pipes (where {CL_DEVICE_PIPE_SUPPORT} is {CL_TRUE}).
     * *ImageBasic*

## `CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR`  (container: `cl_device_info`, value: 0x1036)
- `api/appendix_e.asciidoc`:
     runtime (_sections 4 and 5_):
     
     * Following queries to _table 4.3_
  >> ** {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG},
- `api/opencl_platform_layer.asciidoc`:
     
     If the {cl_khr_fp16_EXT} extension is not supported,
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF} must return 0.
  >> | {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR_anchor}   +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT_anchor}  +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG_anchor}   +
- `api/opencl_platform_layer.asciidoc`:
     
     // The CHAR annotation here is used to convey the same information for all
     // entries in this table row.
  >> [version-note]
     | {cl_uint_TYPE}
     | Returns the native ISA vector width.
     The vector width is defined as the number of scalar elements that

## `CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE`  (container: `cl_device_info`, value: 0x103B)
- `api/appendix_e.asciidoc`:
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT},
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF}
     ** {CL_DEVICE_HOST_UNIFIED_MEMORY}
     ** {CL_DEVICE_OPENCL_C_VERSION}
- `api/opencl_platform_layer.asciidoc`:
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT_anchor}  +
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE_anchor} +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF_anchor}
     
     // The CHAR annotation here is used to convey the same information for all
- `api/opencl_platform_layer.asciidoc`:
     can be stored in the vector.
     
     If double precision is not supported,
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE} must return 0.
     
     If the {cl_khr_fp16_EXT} extension is not supported,
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF} must return 0.

## `CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT`  (container: `cl_device_info`, value: 0x103A)
- `api/appendix_e.asciidoc`:
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG},
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF}
     ** {CL_DEVICE_HOST_UNIFIED_MEMORY}
- `api/opencl_platform_layer.asciidoc`:
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT_anchor}  +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG_anchor}   +
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT_anchor}  +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE_anchor} +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF_anchor}
     

## `CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF`  (container: `cl_device_info`, value: 0x103C)
- `api/appendix_e.asciidoc`:
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE},
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF}
     ** {CL_DEVICE_HOST_UNIFIED_MEMORY}
     ** {CL_DEVICE_OPENCL_C_VERSION}
     * {CL_CONTEXT_NUM_DEVICES} to the list of queries specified to
- `api/opencl_platform_layer.asciidoc`:
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT_anchor}  +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE_anchor} +
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF_anchor}
     
     // The CHAR annotation here is used to convey the same information for all
     // entries in this table row.
- `api/opencl_platform_layer.asciidoc`:
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE} must return 0.
     
     If the {cl_khr_fp16_EXT} extension is not supported,
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF} must return 0.
     | {CL_DEVICE_MAX_CLOCK_FREQUENCY_anchor}
     
     [version-note]

## `CL_DEVICE_NATIVE_VECTOR_WIDTH_INT`  (container: `cl_device_info`, value: 0x1038)
- `api/appendix_e.asciidoc`:
     * Following queries to _table 4.3_
     ** {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT},
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE},
- `api/opencl_platform_layer.asciidoc`:
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF} must return 0.
     | {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR_anchor}   +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT_anchor}  +
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT_anchor}  +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE_anchor} +

## `CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG`  (container: `cl_device_info`, value: 0x1039)
- `api/appendix_e.asciidoc`:
     ** {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT},
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF}
- `api/opencl_platform_layer.asciidoc`:
     | {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR_anchor}   +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT_anchor}  +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT_anchor}    +
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT_anchor}  +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE_anchor} +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF_anchor}

## `CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT`  (container: `cl_device_info`, value: 0x1037)
- `api/appendix_e.asciidoc`:
     
     * Following queries to _table 4.3_
     ** {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR},
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG},
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT},
- `api/opencl_platform_layer.asciidoc`:
     If the {cl_khr_fp16_EXT} extension is not supported,
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF} must return 0.
     | {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR_anchor}   +
  >> {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT_anchor}  +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT_anchor}  +

## `CL_DEVICE_NODE_MASK`  (container: `cl_device_info`, value: 0x106E)
- `api/opencl_platform_layer.asciidoc`:
     {CL_LUID_SIZE_KHR_anchor}
     ifdef::cl_khr_device_uuid[or {CL_LUID_SIZE_KHR_anchor}]
     is the size of the LUID, in bytes.
  >> | {CL_DEVICE_NODE_MASK_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     is the size of the LUID, in bytes.
     | {CL_DEVICE_NODE_MASK_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_device_uuid[]
     or
- `api/opencl_platform_layer.asciidoc`:
     | {cl_uint_TYPE}
     | Returns a node mask for the device.
     
  >> It is not an error to query {CL_DEVICE_NODE_MASK}
     ifdef::cl_khr_device_uuid[or {CL_DEVICE_NODE_MASK_KHR}]
     when {CL_DEVICE_LUID_VALID}
     ifdef::cl_khr_device_uuid[or {CL_DEVICE_LUID_VALID_KHR}]

## `CL_DEVICE_NUMERIC_VERSION`  (container: `cl_device_info`, value: 0x105E)
- `api/appendix_e.asciidoc`:
     version as a numeric value.
     * {CL_PLATFORM_EXTENSIONS_WITH_VERSION} to describe supported
     platform extensions and their supported version.
  >> * {CL_DEVICE_NUMERIC_VERSION} to describe the device version
     as a numeric value.
     * {CL_DEVICE_EXTENSIONS_WITH_VERSION} to describe supported
     device extensions and their supported version.
- `api/opencl_platform_layer.asciidoc`:
     The _major_version.minor_version_ value returned will be one of 1.0,
     1.1, 1.2, 2.0, 2.1, 2.2, 3.0 or 3.1.
     
  >> | {CL_DEVICE_NUMERIC_VERSION_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_NUMERIC_VERSION_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_extended_versioning[]
     or

## `CL_DEVICE_PREFERRED_VECTOR_WIDTH_CHAR`  (container: `cl_device_info`, value: 0x1006)
- `api/opencl_platform_layer.asciidoc`:
     
     The minimum value is 1.
     
  >> | {CL_DEVICE_PREFERRED_VECTOR_WIDTH_CHAR_anchor}   +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_SHORT_anchor}  +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG_anchor}   +

## `CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE`  (container: `cl_device_info`, value: 0x100B)
- `api/opencl_platform_layer.asciidoc`:
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT_anchor}  +
  >> {CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE_anchor} +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF_anchor}
     
     // Manually write this annotation as HALF is an odd-one-out in the table row
- `api/opencl_platform_layer.asciidoc`:
     can be stored in the vector.
     
     If double precision is not supported,
  >> {CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE} must return 0.
     
     If the {cl_khr_fp16_EXT} extension is not supported,
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF} must return 0.

## `CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT`  (container: `cl_device_info`, value: 0x100A)
- `api/opencl_platform_layer.asciidoc`:
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_SHORT_anchor}  +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG_anchor}   +
  >> {CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT_anchor}  +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE_anchor} +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF_anchor}
     

## `CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF`  (container: `cl_device_info`, value: 0x1034)
- `api/opencl_platform_layer.asciidoc`:
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT_anchor}  +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE_anchor} +
  >> {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF_anchor}
     
     // Manually write this annotation as HALF is an odd-one-out in the table row
     // (all other entries were added in OpenCL 1.0).
- `api/opencl_platform_layer.asciidoc`:
     
     // Manually write this annotation as HALF is an odd-one-out in the table row
     // (all other entries were added in OpenCL 1.0).
  >> {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF} is <<unified-spec, missing before>>
     version 1.1.
     | {cl_uint_TYPE}
     | Preferred native vector width size for built-in scalar types that
- `api/opencl_platform_layer.asciidoc`:
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE} must return 0.
     
     If the {cl_khr_fp16_EXT} extension is not supported,
  >> {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF} must return 0.
     | {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR_anchor}   +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT_anchor}  +
     {CL_DEVICE_NATIVE_VECTOR_WIDTH_INT_anchor}    +

## `CL_DEVICE_PREFERRED_VECTOR_WIDTH_INT`  (container: `cl_device_info`, value: 0x1008)
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_PREFERRED_VECTOR_WIDTH_CHAR_anchor}   +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_SHORT_anchor}  +
  >> {CL_DEVICE_PREFERRED_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT_anchor}  +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE_anchor} +

## `CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG`  (container: `cl_device_info`, value: 0x1009)
- `api/opencl_platform_layer.asciidoc`:
     | {CL_DEVICE_PREFERRED_VECTOR_WIDTH_CHAR_anchor}   +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_SHORT_anchor}  +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_INT_anchor}    +
  >> {CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT_anchor}  +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE_anchor} +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF_anchor}

## `CL_DEVICE_PREFERRED_VECTOR_WIDTH_SHORT`  (container: `cl_device_info`, value: 0x1007)
- `api/opencl_platform_layer.asciidoc`:
     The minimum value is 1.
     
     | {CL_DEVICE_PREFERRED_VECTOR_WIDTH_CHAR_anchor}   +
  >> {CL_DEVICE_PREFERRED_VECTOR_WIDTH_SHORT_anchor}  +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_INT_anchor}    +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG_anchor}   +
     {CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT_anchor}  +

## `CL_DEVICE_SINGLE_FP_CONFIG`  (container: `cl_device_info`, value: 0x101B)
- `api/embedded_profile.asciidoc`:
     If double precision is supported i.e. {CL_DEVICE_DOUBLE_FP_CONFIG} is not
     zero, then *cles_khr_int64* must also be supported.
     . The mandated minimum single precision floating-point capability given by
  >> {CL_DEVICE_SINGLE_FP_CONFIG} is {CL_FP_ROUND_TO_ZERO} or
     {CL_FP_ROUND_TO_NEAREST}.
     If {CL_FP_ROUND_TO_NEAREST} is supported, the default rounding mode will
     be round to nearest even; otherwise the default rounding mode will be
- `api/embedded_profile.asciidoc`:
     SPIR-V Environment specifications.
     +
     --
  >> If {CL_FP_INF_NAN} is not set in {CL_DEVICE_SINGLE_FP_CONFIG}, and one of the
     operands or the result of addition, subtraction, multiplication or division
     would signal the overflow or invalid exception (see IEEE 754 specification),
     the value of the result is implementation-defined.
- `api/embedded_profile.asciidoc`:
     The minimum value is 256 bytes.
     
     A maximum of 255 arguments can be passed to a kernel.
  >> | {CL_DEVICE_SINGLE_FP_CONFIG}
     | {cl_device_fp_config_TYPE}
     | Describes single precision floating-point capability of the device.
     This is a bit-field that describes one or more of the following
- `api/opencl_platform_layer.asciidoc`:
     | The minimum value is the size (in bytes) of the largest OpenCL data
     type supported by the device (`long16` in FULL profile, `long16` or
     `int16` in EMBEDDED profile).
  >> | {CL_DEVICE_SINGLE_FP_CONFIG_anchor} footnote:native-rounding-modes[{fn-native-rounding-modes}]
     
     [version-note]
     | {cl_device_fp_config_TYPE}
- `api/opencl_platform_layer.asciidoc`:
     `int16` in EMBEDDED profile).
     | {CL_DEVICE_SINGLE_FP_CONFIG_anchor} footnote:native-rounding-modes[{fn-native-rounding-modes}]
     
  >> [version-note]
     | {cl_device_fp_config_TYPE}
     | Describes single precision floating-point capability of the device.
     This is a bit-field that describes one or more of the following
- `api/opencl_runtime_layer.asciidoc`:
     --
     This option is ignored for single precision numbers if the device does not
     support single precision denormalized numbers i.e. {CL_FP_DENORM} bit is not
  >> set in {CL_DEVICE_SINGLE_FP_CONFIG}.
     
     This option is ignored for double precision numbers if the device does not
     support double precision or if it does support double precision but not

## `CL_DEVICE_SPIRV_CAPABILITIES`  (container: `cl_device_info`, value: 0x12BB)
- `api/opencl_platform_layer.asciidoc`:
     | Returns an array of null-terminated strings, where each string describes
     a SPIR-V extension that is supported by the device.
     
  >> | {CL_DEVICE_SPIRV_CAPABILITIES_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_SPIRV_CAPABILITIES_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_spirv_queries[]
     or

## `CL_DEVICE_SPIRV_EXTENDED_INSTRUCTION_SETS`  (container: `cl_device_info`, value: 0x12B9)
- `api/opencl_platform_layer.asciidoc`:
     extension.
     endif::cl_khr_integer_dot_product[]
     
  >> | {CL_DEVICE_SPIRV_EXTENDED_INSTRUCTION_SETS_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_SPIRV_EXTENDED_INSTRUCTION_SETS_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_spirv_queries[]
     or

## `CL_DEVICE_SPIRV_EXTENSIONS`  (container: `cl_device_info`, value: 0x12BA)
- `api/opencl_platform_layer.asciidoc`:
     | Returns an array of null-terminated strings, where each string describes
     a SPIR-V extended instruction set that is supported by the device.
     
  >> | {CL_DEVICE_SPIRV_EXTENSIONS_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_SPIRV_EXTENSIONS_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_spirv_queries[]
     or

## `CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS`  (container: `cl_device_info`, value: 0x105D)
- `api/appendix_e.asciidoc`:
     * {CL_PLATFORM_HOST_TIMER_RESOLUTION} added to table 4.1 of the API
     specification.
     * {CL_DEVICE_IL_VERSION}, {CL_DEVICE_MAX_NUM_SUB_GROUPS},
  >> {CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS} added to table 4.3 of
     the API specification.
     * {CL_PROGRAM_IL} to table 5.17 of the API specification.
     * {CL_QUEUE_DEVICE_DEFAULT} added to table 5.2 of the API specification.
- `api/appendix_h.asciidoc`:
     | May return `0`, indicating that _device_ does not support sub-groups.
     
     | {clGetDeviceInfo}, passing +
  >> {CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS}
     | Returns {CL_FALSE} if _device_ does not support sub-groups.
     
     | {clGetDeviceInfo}, passing +
- `api/cl_khr_subgroups.asciidoc`:
     * The sub-group OpenCL C built-in functions described by this extension
     must still be accessed as an OpenCL C extension in OpenCL 2.1.
     * Sub-group independent forward progress is an optional device property in
  >> OpenCL 2.1, see {CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS}.
     
     See the link:{OpenCLCSpecURL}#cl_khr_subgroups[Sub-Groups] section of the
     OpenCL C specification for more information.
- `api/opencl_platform_layer.asciidoc`:
     Support for sub-groups is required for an OpenCL 2.1, OpenCL 2.2, or
     OpenCL 3.1 device.
     
  >> | {CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS_anchor}
     
     // Note: This sub-group property is not in cl_khr_subgroups.
     [version-note]
- `api/opencl_platform_layer.asciidoc`:
     | {CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS_anchor}
     
     // Note: This sub-group property is not in cl_khr_subgroups.
  >> [version-note]
     | {cl_bool_TYPE}
     | Is {CL_TRUE} if this device supports independent forward progress of
     sub-groups, {CL_FALSE} otherwise.

## `CL_DEVICE_SVM_TYPE_CAPABILITIES_KHR`  (container: `cl_device_info`, value: 0x1077)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_UUID`  (container: `cl_device_info`, value: 0x106A)
- `api/opencl_platform_layer.asciidoc`:
     | Returns the latest version of the conformance test suite that this device
     has fully passed in accordance with the official conformance process.
     
  >> | {CL_DEVICE_UUID_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     
     | {CL_DEVICE_UUID_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_device_uuid[]
     or

## `CL_DRIVER_UUID`  (container: `cl_device_info`, value: 0x106B)
- `api/opencl_platform_layer.asciidoc`:
     {CL_UUID_SIZE_anchor}
     ifdef::cl_khr_device_uuid[or {CL_UUID_SIZE_KHR_anchor}]
     is the size of the UUID, in bytes.
  >> | {CL_DRIVER_UUID_anchor}
     
     [version-note]
     
- `api/opencl_platform_layer.asciidoc`:
     is the size of the UUID, in bytes.
     | {CL_DRIVER_UUID_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_device_uuid[]
     or

## `CL_FILTER_LINEAR`  (container: `cl_device_info`, value: 0x1141)
- `api/embedded_profile.asciidoc`:
     used with samplers that use a filter mode of {CL_FILTER_NEAREST}.
     The values returned by *read_imagef* footnote:[{fn-readimageh}] for 2D and 3D
     images if `image_channel_data_type` value is {CL_FLOAT} or {CL_HALF_FLOAT}
  >> and sampler with filter_mode = {CL_FILTER_LINEAR} are undefined.
     
     Furthermore, the OpenCL embedded profile has the following restrictions for all
     versions:
- `api/opencl_runtime_layer.asciidoc`:
     {CL_FILTER_NEAREST_anchor} - Returns the image element nearest
     to the image coordinate.
     
  >> {CL_FILTER_LINEAR_anchor} - Returns a weighted average of the
     four image elements nearest to the image coordinate.
     
     The default value is {CL_FILTER_NEAREST}.
- `api/opencl_runtime_layer.asciidoc`:
     {CL_FILTER_NEAREST} - Use the nearest mipmap level to the image
     coordinate.
     
  >> {CL_FILTER_LINEAR} - Use a weighted average of the two mipmap levels
     nearest to the image coordinate.
     
     The default is {CL_FILTER_NEAREST}.
- `env/image_addressing_and_filtering.asciidoc`:
     [[clamp-linear-filtering]]
     ===== Linear Filtering
     
  >> When the filter mode is {CL_FILTER_LINEAR}, a 2 x 2 square of image elements (for a 2D image) or a 2 x 2 x 2 cube of image elements (for a 3D image is
     This 2 x 2 square or 2 x 2 x 2 cube is obtained as follows.
     
     Let:
- `env/image_addressing_and_filtering.asciidoc`:
     [[repeat-linear-filtering]]
     ===== Linear Filtering
     
  >> When filter mode is {CL_FILTER_LINEAR}, a 2 x 2 square of image elements for a 2D image or a 2 x 2 x 2 cube of image elements for a 3D image is select
     This 2 x 2 square or 2 x 2 x 2 cube is obtained as follows.
     
     Let
- `env/image_addressing_and_filtering.asciidoc`:
     [[mirrored-repeat-linear-filtering]]
     ===== Linear Filtering
     
  >> When filter mode is {CL_FILTER_LINEAR}, a 2 x 2 square of image elements for a 2D image or a 2 x 2 x 2 cube of image elements for a 3D image is select
     This 2 x 2 square or 2 x 2 x 2 cube is obtained as follows.
     
     Let

## `CL_FILTER_NEAREST`  (container: `cl_device_info`, value: 0x1140)
- `api/embedded_profile.asciidoc`:
     embedded profile, writes to 2D image arrays are supported.
     . Image and image arrays created with an
     `image_channel_data_type` value of {CL_FLOAT} or {CL_HALF_FLOAT} can only be
  >> used with samplers that use a filter mode of {CL_FILTER_NEAREST}.
     The values returned by *read_imagef* footnote:[{fn-readimageh}] for 2D and 3D
     images if `image_channel_data_type` value is {CL_FLOAT} or {CL_HALF_FLOAT}
     and sampler with filter_mode = {CL_FILTER_LINEAR} are undefined.
- `api/opencl_runtime_layer.asciidoc`:
     image.
     Valid values are:
     
  >> {CL_FILTER_NEAREST_anchor} - Returns the image element nearest
     to the image coordinate.
     
     {CL_FILTER_LINEAR_anchor} - Returns a weighted average of the
- `api/opencl_runtime_layer.asciidoc`:
     {CL_FILTER_LINEAR_anchor} - Returns a weighted average of the
     four image elements nearest to the image coordinate.
     
  >> The default value is {CL_FILTER_NEAREST}.
     ifdef::cl_khr_mipmap_image[]
     | {CL_SAMPLER_MIP_FILTER_MODE_KHR_anchor}
     
- `api/opencl_runtime_layer.asciidoc`:
     image.
     The available filter are:
     
  >> {CL_FILTER_NEAREST} - Use the nearest mipmap level to the image
     coordinate.
     
     {CL_FILTER_LINEAR} - Use a weighted average of the two mipmap levels
- `api/opencl_runtime_layer.asciidoc`:
     {CL_FILTER_LINEAR} - Use a weighted average of the two mipmap levels
     nearest to the image coordinate.
     
  >> The default is {CL_FILTER_NEAREST}.
     | {CL_SAMPLER_LOD_MIN_KHR_anchor}
     
     [version-note]
- `env/image_addressing_and_filtering.asciidoc`:
     [[clamp-nearest_filtering]]
     ===== Nearest Filtering
     
  >> When the filter mode is {CL_FILTER_NEAREST}, the result of the image read instruction is the image element that is nearest (in Manhattan distance) to 
     The image element location `(i,j,k)` is computed as:
     
     [latexmath]

## `CL_KERNEL_ARG_ACCESS_NONE`  (container: `cl_device_info`, value: 0x11A3)
- `api/opencl_runtime_layer.asciidoc`:
     {CL_KERNEL_ARG_ACCESS_READ_ONLY_anchor} +
     {CL_KERNEL_ARG_ACCESS_WRITE_ONLY_anchor} +
     {CL_KERNEL_ARG_ACCESS_READ_WRITE_anchor} +
  >> {CL_KERNEL_ARG_ACCESS_NONE_anchor}
     
     If argument is not an image type and is not declared with the pipe
     qualifier, {CL_KERNEL_ARG_ACCESS_NONE} is returned.
- `api/opencl_runtime_layer.asciidoc`:
     {CL_KERNEL_ARG_ACCESS_NONE_anchor}
     
     If argument is not an image type and is not declared with the pipe
  >> qualifier, {CL_KERNEL_ARG_ACCESS_NONE} is returned.
     If argument is an image type, the access qualifier specified or the
     default access qualifier is returned.
     | {CL_KERNEL_ARG_TYPE_NAME_anchor}

## `CL_KERNEL_ARG_ACCESS_READ_ONLY`  (container: `cl_device_info`, value: 0x11A0)
- `api/opencl_runtime_layer.asciidoc`:
     _arg_index_.
     This can be one of the following values:
     
  >> {CL_KERNEL_ARG_ACCESS_READ_ONLY_anchor} +
     {CL_KERNEL_ARG_ACCESS_WRITE_ONLY_anchor} +
     {CL_KERNEL_ARG_ACCESS_READ_WRITE_anchor} +
     {CL_KERNEL_ARG_ACCESS_NONE_anchor}

## `CL_KERNEL_ARG_ACCESS_READ_WRITE`  (container: `cl_device_info`, value: 0x11A2)
- `api/opencl_runtime_layer.asciidoc`:
     
     {CL_KERNEL_ARG_ACCESS_READ_ONLY_anchor} +
     {CL_KERNEL_ARG_ACCESS_WRITE_ONLY_anchor} +
  >> {CL_KERNEL_ARG_ACCESS_READ_WRITE_anchor} +
     {CL_KERNEL_ARG_ACCESS_NONE_anchor}
     
     If argument is not an image type and is not declared with the pipe

## `CL_KERNEL_ARG_ACCESS_WRITE_ONLY`  (container: `cl_device_info`, value: 0x11A1)
- `api/opencl_runtime_layer.asciidoc`:
     This can be one of the following values:
     
     {CL_KERNEL_ARG_ACCESS_READ_ONLY_anchor} +
  >> {CL_KERNEL_ARG_ACCESS_WRITE_ONLY_anchor} +
     {CL_KERNEL_ARG_ACCESS_READ_WRITE_anchor} +
     {CL_KERNEL_ARG_ACCESS_NONE_anchor}
     

## `CL_KERNEL_ARG_ADDRESS_CONSTANT`  (container: `cl_device_info`, value: 0x119D)
- `api/opencl_runtime_layer.asciidoc`:
     
     {CL_KERNEL_ARG_ADDRESS_GLOBAL_anchor} +
     {CL_KERNEL_ARG_ADDRESS_LOCAL_anchor} +
  >> {CL_KERNEL_ARG_ADDRESS_CONSTANT_anchor} +
     {CL_KERNEL_ARG_ADDRESS_PRIVATE_anchor}
     
     If no address qualifier is specified, the default address qualifier

## `CL_KERNEL_ARG_ADDRESS_GLOBAL`  (container: `cl_device_info`, value: 0x119B)
- `api/opencl_runtime_layer.asciidoc`:
     _arg_index_.
     This can be one of the following values:
     
  >> {CL_KERNEL_ARG_ADDRESS_GLOBAL_anchor} +
     {CL_KERNEL_ARG_ADDRESS_LOCAL_anchor} +
     {CL_KERNEL_ARG_ADDRESS_CONSTANT_anchor} +
     {CL_KERNEL_ARG_ADDRESS_PRIVATE_anchor}

## `CL_KERNEL_ARG_ADDRESS_LOCAL`  (container: `cl_device_info`, value: 0x119C)
- `api/opencl_runtime_layer.asciidoc`:
     This can be one of the following values:
     
     {CL_KERNEL_ARG_ADDRESS_GLOBAL_anchor} +
  >> {CL_KERNEL_ARG_ADDRESS_LOCAL_anchor} +
     {CL_KERNEL_ARG_ADDRESS_CONSTANT_anchor} +
     {CL_KERNEL_ARG_ADDRESS_PRIVATE_anchor}
     

## `CL_KERNEL_ARG_ADDRESS_PRIVATE`  (container: `cl_device_info`, value: 0x119E)
- `api/opencl_runtime_layer.asciidoc`:
     {CL_KERNEL_ARG_ADDRESS_GLOBAL_anchor} +
     {CL_KERNEL_ARG_ADDRESS_LOCAL_anchor} +
     {CL_KERNEL_ARG_ADDRESS_CONSTANT_anchor} +
  >> {CL_KERNEL_ARG_ADDRESS_PRIVATE_anchor}
     
     If no address qualifier is specified, the default address qualifier
     which is {CL_KERNEL_ARG_ADDRESS_PRIVATE} is returned.
- `api/opencl_runtime_layer.asciidoc`:
     {CL_KERNEL_ARG_ADDRESS_PRIVATE_anchor}
     
     If no address qualifier is specified, the default address qualifier
  >> which is {CL_KERNEL_ARG_ADDRESS_PRIVATE} is returned.
     | {CL_KERNEL_ARG_ACCESS_QUALIFIER_anchor}
     
     [version-note]

## `CL_KERNEL_COMPILE_NUM_SUB_GROUPS`  (container: `cl_device_info`, value: 0x11BA)
- `api/appendix_e.asciidoc`:
     runtime (_sections 4 and 5_):
     
     * {clGetKernelSubGroupInfo} API call.
  >> * {CL_KERNEL_MAX_NUM_SUB_GROUPS}, {CL_KERNEL_COMPILE_NUM_SUB_GROUPS}
     additions to table 5.21 of the API specification.
     * {clCreateProgramWithIL} API call.
     * {clGetHostTimer} and {clGetDeviceAndHostTimer} API calls.
- `api/appendix_h.asciidoc`:
     | Returns {CL_INVALID_OPERATION} if no devices associated with _program_ support intermediate language programs.
     
     | {clGetKernelSubGroupInfo}, passing +
  >> {CL_KERNEL_COMPILE_NUM_SUB_GROUPS}
     | Returns `0` if _device_ does not support intermediate language programs, since there is currently no way to require a number of sub-groups per work-
     
     |====
- `api/appendix_h.asciidoc`:
     | Returns {CL_INVALID_OPERATION} if _device_ does not support sub-groups.
     // Note: for {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE}, {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE},
     //       {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT}, {CL_KERNEL_MAX_NUM_SUB_GROUPS},
  >> //       {CL_KERNEL_COMPILE_NUM_SUB_GROUPS}.
     
     |====
     
- `api/opencl_runtime_layer.asciidoc`:
     The returned value may be used to compute a work-group size to
     enqueue the kernel with to give a round number of sub-groups for
     an enqueue.
  >> | {CL_KERNEL_COMPILE_NUM_SUB_GROUPS_anchor}
     
     [version-note]
     
- `api/opencl_runtime_layer.asciidoc`:
     an enqueue.
     | {CL_KERNEL_COMPILE_NUM_SUB_GROUPS_anchor}
     
  >> [version-note]
     
     Also see {cl_khr_subgroups_EXT}.
     | ignored

## `CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM`  (container: `cl_device_info`, value: 0x11B7)
- `api/opencl_runtime_layer.asciidoc`:
     Non-argument pointers to SVM allocations must be specified for
     coarse-grain and fine-grain buffer SVM allocations, but not for
     fine-grain system SVM allocations.
  >> | {CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM_anchor}
     
     [version-note]
     | {cl_bool_TYPE}
- `api/opencl_runtime_layer.asciidoc`:
     fine-grain system SVM allocations.
     | {CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM_anchor}
     
  >> [version-note]
     | {cl_bool_TYPE}
     | Specifies whether the kernel may use pointers to system allocations
     that are not set directly as kernel arguments on devices that support
- `api/opencl_runtime_layer.asciidoc`:
     fine-grain system SVM allocations.
     
     When a device supports fine-grain system SVM allocations and
  >> {CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM} is {CL_TRUE}, the kernel may
     access system allocations that are not set directly as kernel arguments.
     
     Otherwise, if a device does not support fine-grain system SVM
- `api/opencl_runtime_layer.asciidoc`:
     access system allocations that are not set directly as kernel arguments.
     
     Otherwise, if a device does not support fine-grain system SVM
  >> allocations or when {CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM} is
     {CL_FALSE}, behavior is undefined if the kernel accesses a system
     allocation that is not set as a kernel argument.
     
- `api/opencl_runtime_layer.asciidoc`:
     allocation that is not set as a kernel argument.
     
     If {clSetKernelExecInfo} has not been called with a value for
  >> {CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM}, the default value is
     {CL_TRUE}.
     
     ifdef::cl_ext_buffer_device_address[]
- `api/opencl_runtime_layer.asciidoc`:
     * {CL_INVALID_OPERATION} if _param_name is {CL_KERNEL_EXEC_INFO_SVM_PTRS} and
     no devices in the context associated with _kernel_ support SVM.
     * {CL_INVALID_OPERATION} if _param_name_ is
  >> {CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM} and _param_value_ is {CL_TRUE}
     and no devices in the context associated with _kernel_ support fine-grain
     system SVM allocations.
     ifdef::cl_ext_buffer_device_address[]

## `CL_KERNEL_EXEC_INFO_SVM_INDIRECT_ACCESS_KHR`  (container: `cl_device_info`, value: 0x11BB)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_KERNEL_EXEC_INFO_SVM_PTRS`  (container: `cl_device_info`, value: 0x11B6)
- `api/opencl_runtime_layer.asciidoc`:
     [width="100%",cols="<33%,<17%,<50%",options="header"]
     |====
     | Kernel Exec Info | Type | Description
  >> | {CL_KERNEL_EXEC_INFO_SVM_PTRS_anchor}
     
     [version-note]
     | {void_TYPE}*[]
- `api/opencl_runtime_layer.asciidoc`:
     | Kernel Exec Info | Type | Description
     | {CL_KERNEL_EXEC_INFO_SVM_PTRS_anchor}
     
  >> [version-note]
     | {void_TYPE}*[]
     | Specifies a set of pointers to SVM allocations that may be accessed
     by the kernel in addition to those set directly as kernel arguments.
- `api/opencl_runtime_layer.asciidoc`:
     
     Behavior is undefined if the kernel accesses a coarse-grain or
     fine-grain buffer SVM allocation that is not set as a kernel argument
  >> and is not in the set specified by {CL_KERNEL_EXEC_INFO_SVM_PTRS}.
     
     The complete set of pointers is specified by each call to
     {clSetKernelExecInfo} and replaces any previously specified set of
- `api/opencl_runtime_layer.asciidoc`:
     Otherwise, it returns one of the following errors:
     
     * {CL_INVALID_KERNEL} if _kernel_ is a not a valid kernel object.
  >> * {CL_INVALID_OPERATION} if _param_name is {CL_KERNEL_EXEC_INFO_SVM_PTRS} and
     no devices in the context associated with _kernel_ support SVM.
     * {CL_INVALID_OPERATION} if _param_name_ is
     {CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM} and _param_value_ is {CL_TRUE}

## `CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT`  (container: `cl_device_info`, value: 0x11B8)
- `api/appendix_e.asciidoc`:
     * Added table 5.22 to the API specification with the enums:
     {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE},
     {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE} and
  >> {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT}
     
     The following modifications are made to the OpenCL 2.1 platform layer and
     runtime (sections 4 and 5):
- `api/appendix_h.asciidoc`:
     | {clGetKernelSubGroupInfo}
     | Returns {CL_INVALID_OPERATION} if _device_ does not support sub-groups.
     // Note: for {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE}, {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE},
  >> //       {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT}, {CL_KERNEL_MAX_NUM_SUB_GROUPS},
     //       {CL_KERNEL_COMPILE_NUM_SUB_GROUPS}.
     
     |====
- `api/opencl_runtime_layer.asciidoc`:
     dispatch.
     The number of dimensions in the ND-range will be inferred from
     the value specified for _input_value_size_.
  >> | {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT_anchor}
     
     [version-note]
     
- `api/opencl_runtime_layer.asciidoc`:
     the value specified for _input_value_size_.
     | {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT_anchor}
     
  >> [version-note]
     
     Also see {cl_khr_subgroups_EXT}.
     | {size_t_TYPE}
- `api/opencl_runtime_layer.asciidoc`:
     * {CL_INVALID_VALUE} if _param_name_ is
     {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE},
     {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE} or
  >> {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT} and the size in bytes specified
     by _input_value_size_ is not valid or if _input_value_ is `NULL`.
     * {CL_OUT_OF_RESOURCES} if there is a failure to allocate resources required
     by the OpenCL implementation on the device.

## `CL_KERNEL_MAX_NUM_SUB_GROUPS`  (container: `cl_device_info`, value: 0x11B9)
- `api/appendix_e.asciidoc`:
     runtime (_sections 4 and 5_):
     
     * {clGetKernelSubGroupInfo} API call.
  >> * {CL_KERNEL_MAX_NUM_SUB_GROUPS}, {CL_KERNEL_COMPILE_NUM_SUB_GROUPS}
     additions to table 5.21 of the API specification.
     * {clCreateProgramWithIL} API call.
     * {clGetHostTimer} and {clGetDeviceAndHostTimer} API calls.
- `api/appendix_h.asciidoc`:
     | {clGetKernelSubGroupInfo}
     | Returns {CL_INVALID_OPERATION} if _device_ does not support sub-groups.
     // Note: for {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE}, {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE},
  >> //       {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT}, {CL_KERNEL_MAX_NUM_SUB_GROUPS},
     //       {CL_KERNEL_COMPILE_NUM_SUB_GROUPS}.
     
     |====
- `api/opencl_runtime_layer.asciidoc`:
     If no work-group size can accommodate the requested number of
     sub-groups, 0 will be returned in each element of the return
     array.
  >> | {CL_KERNEL_MAX_NUM_SUB_GROUPS_anchor}
     
     [version-note]
     
- `api/opencl_runtime_layer.asciidoc`:
     array.
     | {CL_KERNEL_MAX_NUM_SUB_GROUPS_anchor}
     
  >> [version-note]
     
     Also see {cl_khr_subgroups_EXT}.
     | ignored

## `CL_MEM_OBJECT_BUFFER`  (container: `cl_device_info`, value: 0x10F0)
- `api/cl_khr_external_memory_android_hardware_buffer.asciidoc`:
     | `AHARDWAREBUFFER_FORMAT_BLOB`
     | `N/A`
     | `N/A`
  >> | {CL_MEM_OBJECT_BUFFER}
     |===
     
     [[cl_khr_external_memory_android_hardware_buffer-Sample-Code]]
- `api/opencl_runtime_layer.asciidoc`:
     | {cl_mem_object_type_TYPE}
     | Returns one of the following values:
     
  >> {CL_MEM_OBJECT_BUFFER_anchor} if _memobj_ is created with {clCreateBuffer},
     {clCreateBufferWithProperties}, or {clCreateSubBuffer}.
     
     {CL_MEM_OBJECT_IMAGE2D} if _memobj_ is created with {clCreateImage2D}.
- `extensions/cl_pocl_content_size.asciidoc`:
     
     The user is responsible for maintaining the correct meaningful byte count (the implementation does not update the _content_size_buffer_).
     
  >> _buffer_ is a valid cl_mem object of `CL_MEM_OBJECT_BUFFER` type.
     
     _content_size_buffer_ is a valid cl_mem object of `CL_MEM_OBJECT_BUFFER` type. _content_size_buffer_ must be at least 64bits large. The meaningful byt
     
- `extensions/cl_pocl_content_size.asciidoc`:
     
     _buffer_ is a valid cl_mem object of `CL_MEM_OBJECT_BUFFER` type.
     
  >> _content_size_buffer_ is a valid cl_mem object of `CL_MEM_OBJECT_BUFFER` type. _content_size_buffer_ must be at least 64bits large. The meaningful byt
     
     *clSetContentSizeBufferPoCL* returns `CL_SUCCESS` if the function is executed successfully, otherwise it returns one of the following errors:
     
- `extensions/cl_pocl_content_size.asciidoc`:
     *clSetContentSizeBufferPoCL* returns `CL_SUCCESS` if the function is executed successfully, otherwise it returns one of the following errors:
     
     * `CL_INVALID_MEM_OBJECT` if _buffer_ or _content_size_buffer_ are not a valid mem objects.
  >> * `CL_INVALID_VALUE` if _buffer_ or _content_size_buffer_ are not of `CL_MEM_OBJECT_BUFFER` type, or _content_size_buffer_ is too small.
     * `CL_INVALID_CONTEXT` if _buffer_ and _content_size_buffer_ are not in the same context.
     * `CL_OUT_OF_RESOURCES` if there is a failure to allocate resources required by the OpenCL implementation on the device.
     * `CL_OUT_OF_HOST_MEMORY` if there is a failure to allocate resources required by the OpenCL implementation on the host.

## `CL_MEM_OBJECT_IMAGE1D`  (container: `cl_device_info`, value: 0x10F4)
- `api/opencl_runtime_layer.asciidoc`:
     [width="100%",cols="<50%,<50%",options="header"]
     |====
     | Image Type | Size of buffer that _host_ptr_ points to
  >> | {CL_MEM_OBJECT_IMAGE1D_anchor}
     
     [version-note]
     | {geq} image_row_pitch
- `api/opencl_runtime_layer.asciidoc`:
     | Image Type | Size of buffer that _host_ptr_ points to
     | {CL_MEM_OBJECT_IMAGE1D_anchor}
     
  >> [version-note]
     | {geq} image_row_pitch
     | {CL_MEM_OBJECT_IMAGE1D_BUFFER_anchor}
     
- `api/opencl_runtime_layer.asciidoc`:
     [version-note]
     
     * _image_type_ describes the image type and must be either
  >> {CL_MEM_OBJECT_IMAGE1D}, {CL_MEM_OBJECT_IMAGE1D_BUFFER},
     {CL_MEM_OBJECT_IMAGE1D_ARRAY}, {CL_MEM_OBJECT_IMAGE2D},
     {CL_MEM_OBJECT_IMAGE2D_ARRAY}, or {CL_MEM_OBJECT_IMAGE3D}.
     * _image_width_ is the width of the image in pixels.
- `api/opencl_runtime_layer.asciidoc`:
     endif::cl_ext_immutable_memory_objects[]
     Please see <<image-format-mapping, Image Format Mapping>> for clarification.
     * _image_type_ describes the image type and must be either
  >> {CL_MEM_OBJECT_IMAGE1D}, {CL_MEM_OBJECT_IMAGE1D_BUFFER}, {CL_MEM_OBJECT_IMAGE2D},
     {CL_MEM_OBJECT_IMAGE3D}, {CL_MEM_OBJECT_IMAGE1D_ARRAY}, or
     {CL_MEM_OBJECT_IMAGE2D_ARRAY}.
     * _num_entries_ specifies the number of entries that can be returned in the
- `api/opencl_runtime_layer.asciidoc`:
     Additionally:
     
     * If the kernel argument is a 1D image, then the image memory object must be of
  >> image type {CL_MEM_OBJECT_IMAGE1D}.
     * If the kernel argument is a 2D image, then the image memory object must be of
     image type {CL_MEM_OBJECT_IMAGE2D}.
     * If the kernel argument is a 3D image, then the image memory object must be of

## `CL_MEM_OBJECT_IMAGE1D_ARRAY`  (container: `cl_device_info`, value: 0x10F5)
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | {geq} image_slice_pitch {times} image_depth
  >> | {CL_MEM_OBJECT_IMAGE1D_ARRAY_anchor}
     
     [version-note]
     | {geq} image_slice_pitch {times} image_array_size
- `api/opencl_runtime_layer.asciidoc`:
     | {geq} image_slice_pitch {times} image_depth
     | {CL_MEM_OBJECT_IMAGE1D_ARRAY_anchor}
     
  >> [version-note]
     | {geq} image_slice_pitch {times} image_array_size
     | {CL_MEM_OBJECT_IMAGE2D_ARRAY_anchor}
     
- `api/opencl_runtime_layer.asciidoc`:
     
     * _image_type_ describes the image type and must be either
     {CL_MEM_OBJECT_IMAGE1D}, {CL_MEM_OBJECT_IMAGE1D_BUFFER},
  >> {CL_MEM_OBJECT_IMAGE1D_ARRAY}, {CL_MEM_OBJECT_IMAGE2D},
     {CL_MEM_OBJECT_IMAGE2D_ARRAY}, or {CL_MEM_OBJECT_IMAGE3D}.
     * _image_width_ is the width of the image in pixels.
     For a 1D image, 1D image array, 2D image, or 2D image array, the image width
- `api/opencl_runtime_layer.asciidoc`:
     Please see <<image-format-mapping, Image Format Mapping>> for clarification.
     * _image_type_ describes the image type and must be either
     {CL_MEM_OBJECT_IMAGE1D}, {CL_MEM_OBJECT_IMAGE1D_BUFFER}, {CL_MEM_OBJECT_IMAGE2D},
  >> {CL_MEM_OBJECT_IMAGE3D}, {CL_MEM_OBJECT_IMAGE1D_ARRAY}, or
     {CL_MEM_OBJECT_IMAGE2D_ARRAY}.
     * _num_entries_ specifies the number of entries that can be returned in the
     memory location given by _image_formats_.
- `api/opencl_runtime_layer.asciidoc`:
     except `mem_object` may be `0` to require that the value returned be supported
     for all possible values of the members that are set to `0`. +
     If _image_desc_ is not `NULL`, then _image_type_ must be either `0`,
  >> {CL_MEM_OBJECT_IMAGE1D_ARRAY} or {CL_MEM_OBJECT_IMAGE2D_ARRAY}, otherwise
     {CL_INVALID_IMAGE_DESCRIPTOR} is returned. +
     // TODO: should we require _image_array_size_ to be `0`?
     
- `api/opencl_runtime_layer.asciidoc`:
     * If the kernel argument is a 1D image buffer, then the image memory object must
     be of image type {CL_MEM_OBJECT_IMAGE1D_BUFFER}.
     * If the kernel argument is a 1D image array, then the image memory object must
  >> be of image type {CL_MEM_OBJECT_IMAGE1D_ARRAY}.
     * If the kernel argument is a 2D image array, then the image memory object must
     be of image type {CL_MEM_OBJECT_IMAGE2D_ARRAY}.
     * If the kernel argument is a 2D depth image, then the image memory object must

## `CL_MEM_OBJECT_IMAGE1D_BUFFER`  (container: `cl_device_info`, value: 0x10F6)
- `api/cl_ext_image_requirements_info.asciidoc`:
     . Consistency checks for {CL_IMAGE_REQUIREMENTS_MAX_WIDTH_EXT}
     * For all image formats, image types and a selection of values for other members in _image_desc_ (that MUST include `0`)
     ** Check that the {CL_IMAGE_REQUIREMENTS_MAX_WIDTH_EXT} query can be performed successfully
  >> ** Check that the value is smaller than or equal to the value returned for {CL_DEVICE_IMAGE_MAX_BUFFER_SIZE} for images of {CL_MEM_OBJECT_IMAGE1D_BUFF
     
     . Negative tests for {CL_IMAGE_REQUIREMENTS_MAX_HEIGHT_EXT}
     * Attempt to perform the {CL_IMAGE_REQUIREMENTS_MAX_HEIGHT_EXT} query on all image types for which it is not valid
- `api/opencl_runtime_layer.asciidoc`:
     The alignment requirements for data stored in image objects are described
     in <<alignment-app-data-types,Alignment of Application Data Types>>.
     
  >> For all image types except {CL_MEM_OBJECT_IMAGE1D_BUFFER}, if the value
     specified for _flags_ is 0, the default is used which is {CL_MEM_READ_WRITE}.
     
     For {CL_MEM_OBJECT_IMAGE1D_BUFFER} image type, or an image created from
- `api/opencl_runtime_layer.asciidoc`:
     For all image types except {CL_MEM_OBJECT_IMAGE1D_BUFFER}, if the value
     specified for _flags_ is 0, the default is used which is {CL_MEM_READ_WRITE}.
     
  >> For {CL_MEM_OBJECT_IMAGE1D_BUFFER} image type, or an image created from
     another memory object (image or buffer), if the {CL_MEM_READ_WRITE},
     {CL_MEM_READ_ONLY} or {CL_MEM_WRITE_ONLY} values are not specified in _flags_,
     they are inherited from the corresponding memory access qualifiers associated
- `api/opencl_runtime_layer.asciidoc`:
     * {CL_MEM_USE_HOST_PTR} or {CL_MEM_COPY_HOST_PTR} cannot be specified if a
     mipmapped image is created.
     * The _host_ptr_ argument to {clCreateImage} must be a `NULL` value.
  >> * Mip-mapped images cannot be created for {CL_MEM_OBJECT_IMAGE1D_BUFFER}
     images, depth images or multi-sampled (i.e. msaa) images.
     endif::cl_khr_mipmap_image[]
     
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | {geq} image_row_pitch
  >> | {CL_MEM_OBJECT_IMAGE1D_BUFFER_anchor}
     
     [version-note]
     | {geq} image_row_pitch
- `api/opencl_runtime_layer.asciidoc`:
     | {geq} image_row_pitch
     | {CL_MEM_OBJECT_IMAGE1D_BUFFER_anchor}
     
  >> [version-note]
     | {geq} image_row_pitch
     | {CL_MEM_OBJECT_IMAGE2D_anchor}
     

## `CL_MEM_OBJECT_IMAGE2D`  (container: `cl_device_info`, value: 0x10F1)
- `api/appendix_h.asciidoc`:
     
     | {clCreateImage} or +
     {clCreateImageWithProperties}, passing +
  >> __image_type__ equal to {CL_MEM_OBJECT_IMAGE2D} and +
     __mem_object__ not equal to `NULL`
     | Returns {CL_INVALID_OPERATION} if no devices in _context_ support creating a 2D image from a buffer.
     
- `api/cl_khr_external_memory_android_hardware_buffer.asciidoc`:
     | `AHARDWAREBUFFER_FORMAT_R8G8B8A8_UNORM`
     | {CL_RGBA}
     | {CL_UNORM_INT8}
  >> | Image, e.g. {CL_MEM_OBJECT_IMAGE2D}
     
     | `AHARDWAREBUFFER_FORMAT_R16G16B16A16_FLOAT`
     | {CL_RGBA}
- `api/cl_khr_external_memory_android_hardware_buffer.asciidoc`:
     | `AHARDWAREBUFFER_FORMAT_R16G16B16A16_FLOAT`
     | {CL_RGBA}
     | {CL_HALF_FLOAT}
  >> | Image, e.g. {CL_MEM_OBJECT_IMAGE2D}
     
     | `AHARDWAREBUFFER_FORMAT_R8_UNORM`
     | {CL_R}
- `api/cl_khr_external_memory_android_hardware_buffer.asciidoc`:
     | `AHARDWAREBUFFER_FORMAT_R8_UNORM`
     | {CL_R}
     | {CL_UNORM_INT8}
  >> | Image, e.g. {CL_MEM_OBJECT_IMAGE2D}
     
     | `AHARDWAREBUFFER_FORMAT_BLOB`
     | `N/A`
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | {geq} image_row_pitch
  >> | {CL_MEM_OBJECT_IMAGE2D_anchor}
     
     [version-note]
     | {geq} image_row_pitch {times} image_height
- `api/opencl_runtime_layer.asciidoc`:
     | {geq} image_row_pitch
     | {CL_MEM_OBJECT_IMAGE2D_anchor}
     
  >> [version-note]
     | {geq} image_row_pitch {times} image_height
     | {CL_MEM_OBJECT_IMAGE3D_anchor}
     

## `CL_MEM_OBJECT_IMAGE2D_ARRAY`  (container: `cl_device_info`, value: 0x10F3)
- `api/cl_khr_external_memory.asciidoc`:
     // Set cl_image_desc based on external image info
     size_t clImageFormatSize;
     cl_image_desc image_desc = { };
  >> image_desc.image_type = CL_MEM_OBJECT_IMAGE2D_ARRAY;
     image_desc.image_width = width;
     image_desc.image_height = height;
     image_desc.image_depth = depth;
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | {geq} image_slice_pitch {times} image_array_size
  >> | {CL_MEM_OBJECT_IMAGE2D_ARRAY_anchor}
     
     [version-note]
     | {geq} image_slice_pitch {times} image_array_size
- `api/opencl_runtime_layer.asciidoc`:
     | {geq} image_slice_pitch {times} image_array_size
     | {CL_MEM_OBJECT_IMAGE2D_ARRAY_anchor}
     
  >> [version-note]
     | {geq} image_slice_pitch {times} image_array_size
     |====
     
- `api/opencl_runtime_layer.asciidoc`:
     * _image_type_ describes the image type and must be either
     {CL_MEM_OBJECT_IMAGE1D}, {CL_MEM_OBJECT_IMAGE1D_BUFFER},
     {CL_MEM_OBJECT_IMAGE1D_ARRAY}, {CL_MEM_OBJECT_IMAGE2D},
  >> {CL_MEM_OBJECT_IMAGE2D_ARRAY}, or {CL_MEM_OBJECT_IMAGE3D}.
     * _image_width_ is the width of the image in pixels.
     For a 1D image, 1D image array, 2D image, or 2D image array, the image width
     must be greater than or equal to one and less than or equal to the
- `api/opencl_runtime_layer.asciidoc`:
     * _image_type_ describes the image type and must be either
     {CL_MEM_OBJECT_IMAGE1D}, {CL_MEM_OBJECT_IMAGE1D_BUFFER}, {CL_MEM_OBJECT_IMAGE2D},
     {CL_MEM_OBJECT_IMAGE3D}, {CL_MEM_OBJECT_IMAGE1D_ARRAY}, or
  >> {CL_MEM_OBJECT_IMAGE2D_ARRAY}.
     * _num_entries_ specifies the number of entries that can be returned in the
     memory location given by _image_formats_.
     * _image_formats_ is a pointer to a memory location where the list of
- `api/opencl_runtime_layer.asciidoc`:
     except `mem_object` may be `0` to require that the value returned be supported
     for all possible values of the members that are set to `0`. +
     If _image_desc_ is not `NULL`, then _image_type_ must be either `0`,
  >> {CL_MEM_OBJECT_IMAGE2D}, {CL_MEM_OBJECT_IMAGE2D_ARRAY}, or {CL_MEM_OBJECT_IMAGE3D},
     otherwise {CL_INVALID_IMAGE_DESCRIPTOR} is returned. +
     // TODO: should we require _image_height_ to be `0`?
     

## `CL_MEM_OBJECT_IMAGE3D`  (container: `cl_device_info`, value: 0x10F2)
- `api/appendix_h.asciidoc`:
     | Will not describe support for the {cl_khr_3d_image_writes_EXT} extension if _device_ does not support writing to 3D image objects.
     
     | {clGetSupportedImageFormats}, passing +
  >> {CL_MEM_OBJECT_IMAGE3D} and one of +
     {CL_MEM_WRITE_ONLY}, +
     {CL_MEM_READ_WRITE}, or +
     {CL_MEM_KERNEL_READ_AND_WRITE}
- `api/cl_ext_image_requirements_info.asciidoc`:
     . Consistency checks for {CL_IMAGE_REQUIREMENTS_MAX_WIDTH_EXT}
     * For all image formats, image types and a selection of values for other members in _image_desc_ (that MUST include `0`)
     ** Check that the {CL_IMAGE_REQUIREMENTS_MAX_WIDTH_EXT} query can be performed successfully
  >> ** Check that the value is smaller than or equal to the value returned for {CL_DEVICE_IMAGE_MAX_BUFFER_SIZE} for images of {CL_MEM_OBJECT_IMAGE1D_BUFF
     
     . Negative tests for {CL_IMAGE_REQUIREMENTS_MAX_HEIGHT_EXT}
     * Attempt to perform the {CL_IMAGE_REQUIREMENTS_MAX_HEIGHT_EXT} query on all image types for which it is not valid
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | {geq} image_row_pitch {times} image_height
  >> | {CL_MEM_OBJECT_IMAGE3D_anchor}
     
     [version-note]
     | {geq} image_slice_pitch {times} image_depth
- `api/opencl_runtime_layer.asciidoc`:
     | {geq} image_row_pitch {times} image_height
     | {CL_MEM_OBJECT_IMAGE3D_anchor}
     
  >> [version-note]
     | {geq} image_slice_pitch {times} image_depth
     | {CL_MEM_OBJECT_IMAGE1D_ARRAY_anchor}
     
- `api/opencl_runtime_layer.asciidoc`:
     _image_row_pitch_.
     * _host_ptr_ is a pointer to the image data that may already be allocated by
     the application.
  >> Refer to the {CL_MEM_OBJECT_IMAGE3D} entry in the
     <<host-ptr-buffer-size-table, required _host_ptr_ buffer size table>> for a
     description of how large the buffer that _host_ptr_ points to must be.
     The image data specified by _host_ptr_ is stored as a linear sequence of
- `api/opencl_runtime_layer.asciidoc`:
     * _image_type_ describes the image type and must be either
     {CL_MEM_OBJECT_IMAGE1D}, {CL_MEM_OBJECT_IMAGE1D_BUFFER},
     {CL_MEM_OBJECT_IMAGE1D_ARRAY}, {CL_MEM_OBJECT_IMAGE2D},
  >> {CL_MEM_OBJECT_IMAGE2D_ARRAY}, or {CL_MEM_OBJECT_IMAGE3D}.
     * _image_width_ is the width of the image in pixels.
     For a 1D image, 1D image array, 2D image, or 2D image array, the image width
     must be greater than or equal to one and less than or equal to the

## `CL_MEM_OBJECT_PIPE`  (container: `cl_device_info`, value: 0x10F7)
- `api/opencl_runtime_layer.asciidoc`:
     The value of __image_desc__->__image_type__ if _memobj_ is created with
     {clCreateImage} or {clCreateImageWithProperties}.
     
  >> {CL_MEM_OBJECT_PIPE_anchor} if _memobj_ is created with {clCreatePipe}.
     | {CL_MEM_FLAGS_anchor}
     
     [version-note]

## `CL_PROGRAM_IL`  (container: `cl_device_info`, value: 0x1169)
- `api/appendix_e.asciidoc`:
     * {CL_DEVICE_IL_VERSION}, {CL_DEVICE_MAX_NUM_SUB_GROUPS},
     {CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS} added to table 4.3 of
     the API specification.
  >> * {CL_PROGRAM_IL} to table 5.17 of the API specification.
     * {CL_QUEUE_DEVICE_DEFAULT} added to table 5.2 of the API specification.
     * Added table 5.22 to the API specification with the enums:
     {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE},
- `api/appendix_h.asciidoc`:
     | May return an empty string and empty array, indicating that _device_ does not support intermediate language programs.
     
     | {clGetProgramInfo}, passing +
  >> {CL_PROGRAM_IL}
     | Returns an empty buffer (such as _param_value_size_ret_ equal to `0`) if no devices in the context associated with _program_ support intermediate la
     
     | {clCreateProgramWithIL}
- `api/opencl_runtime_layer.asciidoc`:
     The total number of characters that represents the program source
     code, including the null terminator, is returned in
     _param_value_size_ret_.
  >> | {CL_PROGRAM_IL_anchor}
     
     [version-note]
     
- `api/opencl_runtime_layer.asciidoc`:
     _param_value_size_ret_.
     | {CL_PROGRAM_IL_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_il_program[]
     {CL_PROGRAM_IL_KHR_anchor}

## `CL_RGBx`  (container: `cl_device_info`, value: 0x10BC)
- `api/appendix_c.asciidoc`:
     The user is also responsible for ensuring image data passed is aligned to
     the granularity of the data representing a single pixel (e.g.
     `image_num_channels * sizeof(image_channel_data_type)`) except for {CL_RGB}
  >> and {CL_RGBx} images where the data must be aligned to the granularity of a
     single channel in a pixel (i.e. `sizeof(image_channel_data_type)`).
     This implies that OpenCL images created with {CL_MEM_USE_HOST_PTR} must align
     correctly.
- `api/appendix_e.asciidoc`:
     ** {CL_DEVICE_OPENCL_C_VERSION}
     * {CL_CONTEXT_NUM_DEVICES} to the list of queries specified to
     {clGetContextInfo}.
  >> * Optional image formats: {CL_Rx}, {CL_RGx}, and {CL_RGBx}.
     * Support for sub-buffer objects ability to create a buffer object that
     refers to a specific region in another buffer object using
     {clCreateSubBuffer}.
- `api/opencl_runtime_layer.asciidoc`:
     // other entries in this row were in OpenCL 1.0).
     {CL_ABGR} is <<unified-spec, missing before>> version 2.0.
     | Four channel image formats, where the four channels represent `RED`, `GREEN`, `BLUE`, and `ALPHA` components.
  >> | {CL_RGBx_anchor}
     
     [version-note]
     | A four channel image format, where the first three channels represent `RED`, `GREEN`, and `BLUE` components and the fourth channel is ignored.
- `api/opencl_runtime_layer.asciidoc`:
     | Four channel image formats, where the four channels represent `RED`, `GREEN`, `BLUE`, and `ALPHA` components.
     | {CL_RGBx_anchor}
     
  >> [version-note]
     | A four channel image format, where the first three channels represent `RED`, `GREEN`, and `BLUE` components and the fourth channel is ignored.
     | {CL_sRGB_anchor}
     
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | Represents a normalized 5-6-5 3-channel RGB image.
  >> The channel order must be {CL_RGB} or {CL_RGBx}.
     | {CL_UNORM_SHORT_555_anchor}
     
     [version-note]
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | Represents a normalized x-5-5-5 4-channel xRGB image.
  >> The channel order must be {CL_RGB} or {CL_RGBx}.
     | {CL_UNORM_INT_101010_anchor}
     
     [version-note]

## `CL_RGx`  (container: `cl_device_info`, value: 0x10BB)
- `api/appendix_e.asciidoc`:
     ** {CL_DEVICE_OPENCL_C_VERSION}
     * {CL_CONTEXT_NUM_DEVICES} to the list of queries specified to
     {clGetContextInfo}.
  >> * Optional image formats: {CL_Rx}, {CL_RGx}, and {CL_RGBx}.
     * Support for sub-buffer objects ability to create a buffer object that
     refers to a specific region in another buffer object using
     {clCreateSubBuffer}.
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | A three channel image format, where the three channels represent `RED`, `GREEN`, and `BLUE` components.
  >> | {CL_RGx_anchor}
     
     [version-note]
     | A three channel image format, where the first two channels represent `RED` and `GREEN` components and the third channel is ignored.
- `api/opencl_runtime_layer.asciidoc`:
     | A three channel image format, where the three channels represent `RED`, `GREEN`, and `BLUE` components.
     | {CL_RGx_anchor}
     
  >> [version-note]
     | A three channel image format, where the first two channels represent `RED` and `GREEN` components and the third channel is ignored.
     | {CL_RGBA_anchor}, {CL_ARGB_anchor}, {CL_BGRA_anchor}, {CL_ABGR_anchor}
     
- `env/common_properties.asciidoc`:
     
     | 11
     | *RGx*
  >> | {CL_RGx}
     
     | 12
     | *RGBx*

## `CL_Rx`  (container: `cl_device_info`, value: 0x10BA)
- `api/appendix_e.asciidoc`:
     ** {CL_DEVICE_OPENCL_C_VERSION}
     * {CL_CONTEXT_NUM_DEVICES} to the list of queries specified to
     {clGetContextInfo}.
  >> * Optional image formats: {CL_Rx}, {CL_RGx}, and {CL_RGBx}.
     * Support for sub-buffer objects ability to create a buffer object that
     refers to a specific region in another buffer object using
     {clCreateSubBuffer}.
- `api/opencl_runtime_layer.asciidoc`:
     | Two channel image formats.
     The first channel always represents a `RED` component.
     The second channel represents a `GREEN` component or an `ALPHA` component.
  >> | {CL_Rx_anchor}
     
     [version-note]
     | A two channel image format, where the first channel represents a `RED`
- `api/opencl_runtime_layer.asciidoc`:
     The second channel represents a `GREEN` component or an `ALPHA` component.
     | {CL_Rx_anchor}
     
  >> [version-note]
     | A two channel image format, where the first channel represents a `RED`
     component and the second channel is ignored.
     
- `env/common_properties.asciidoc`:
     
     | 10
     | *Rx*
  >> | {CL_Rx}
     
     | 11
     | *RGx*

## `CL_SAMPLER_LOD_MAX`  (container: `cl_device_info`, value: 0x1157)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SAMPLER_LOD_MIN`  (container: `cl_device_info`, value: 0x1156)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SAMPLER_MIP_FILTER_MODE`  (container: `cl_device_info`, value: 0x1155)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_UNSIGNED_INT_RAW10_EXT`  (container: `cl_device_info`, value: 0x10E3)
- `extensions/cl_ext_image_raw10_raw12.asciidoc`:
     
     [source,c]
     ----
  >> CL_UNSIGNED_INT_RAW10_EXT       0x10E3
     CL_UNSIGNED_INT_RAW12_EXT       0x10E4
     ----
     
- `extensions/cl_ext_image_raw10_raw12.asciidoc`:
     | Image Channel Data Type
     | Description
     
  >> | {CL_UNSIGNED_INT_RAW10_EXT}
     | Each channel component is an unnormalized unsigned 10-bit integer value.
     The channel order must be {CL_R}.
     
- `extensions/cl_ext_image_raw10_raw12.asciidoc`:
     (Add the following to Section 5.3.1.1, _Image Format Descriptor_) ::
     +
     --
  >> If `image_channel_data_type` = {CL_UNSIGNED_INT_RAW10_EXT}, pixel data is densely
     packed in each row and each 4 consecutive pixels are packed into 5 bytes. Each one
     of the first 4 bytes contains the top 8 bits of each pixel, the fifth byte
     contains the 2 least significant bits of the 4 pixels. The memory layout of
- `extensions/cl_ext_image_raw10_raw12.asciidoc`:
     Add the following to the description of `image_width`:
     
     The image width must be a multiple of 4 for images `image_channel_data_type`
  >> is {CL_UNSIGNED_INT_RAW10_EXT}. The image width must be a multiple of 2 for
     images `image_channel_data_type` is {CL_UNSIGNED_INT_RAW12_EXT}.
     --
     

## `CL_UNSIGNED_INT_RAW12_EXT`  (container: `cl_device_info`, value: 0x10E4)
- `extensions/cl_ext_image_raw10_raw12.asciidoc`:
     [source,c]
     ----
     CL_UNSIGNED_INT_RAW10_EXT       0x10E3
  >> CL_UNSIGNED_INT_RAW12_EXT       0x10E4
     ----
     
     == New OpenCL C Feature Names
- `extensions/cl_ext_image_raw10_raw12.asciidoc`:
     | Each channel component is an unnormalized unsigned 10-bit integer value.
     The channel order must be {CL_R}.
     
  >> | {CL_UNSIGNED_INT_RAW12_EXT}
     | Each channel component is an unnormalized unsigned 12-bit integer value.
     The channel order must be {CL_R}.
     
- `extensions/cl_ext_image_raw10_raw12.asciidoc`:
     
     |====
     
  >> If `image_channel_data_type` = {CL_UNSIGNED_INT_RAW12_EXT}, pixel data is densely
     packed in each row and each 2 consecutive pixels are packed into 3 bytes. The
     first and second byte contains the top 8 bits of first and second pixel. The
     third byte contains the 4 least significant bits of the two pixels, the memory
- `extensions/cl_ext_image_raw10_raw12.asciidoc`:
     
     The image width must be a multiple of 4 for images `image_channel_data_type`
     is {CL_UNSIGNED_INT_RAW10_EXT}. The image width must be a multiple of 2 for
  >> images `image_channel_data_type` is {CL_UNSIGNED_INT_RAW12_EXT}.
     --
     
     --

## `CL_sBGRA`  (container: `cl_device_info`, value: 0x10C2)
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | A three channel image format, where the three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
  >> | {CL_sRGBA_anchor}, {CL_sBGRA_anchor}
     
     // The CL_sRGBA annotation here is used to convey the same information for both
     // entries in this table row.
- `api/opencl_runtime_layer.asciidoc`:
     |====
     | Image Channel Order in _image_format_:
     | Image Channel Order associated with `mem_object`:
  >> | {CL_sBGRA}
     | {CL_BGRA}
     | {CL_BGRA}
     | {CL_sBGRA}
- `api/opencl_runtime_layer.asciidoc`:
     | {CL_sBGRA}
     | {CL_BGRA}
     | {CL_BGRA}
  >> | {CL_sBGRA}
     | {CL_sRGBA}
     | {CL_RGBA}
     | {CL_RGBA}
- `env/common_properties.asciidoc`:
     
     | 18
     | *sBGRA*
  >> | `CL_sBGRA`
     
     | 19
     | *ABGR*

## `CL_sRGB`  (container: `cl_device_info`, value: 0x10BF)
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | A four channel image format, where the first three channels represent `RED`, `GREEN`, and `BLUE` components and the fourth channel is ignored.
  >> | {CL_sRGB_anchor}
     
     [version-note]
     | A three channel image format, where the three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
- `api/opencl_runtime_layer.asciidoc`:
     | A four channel image format, where the first three channels represent `RED`, `GREEN`, and `BLUE` components and the fourth channel is ignored.
     | {CL_sRGB_anchor}
     
  >> [version-note]
     | A three channel image format, where the three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
     | {CL_sRGBA_anchor}, {CL_sBGRA_anchor}
     
- `api/opencl_runtime_layer.asciidoc`:
     | {CL_RGBA}
     | {CL_RGBA}
     | {CL_sRGBA}
  >> | {CL_sRGB}
     | {CL_RGB}
     | {CL_RGB}
     | {CL_sRGB}
- `api/opencl_runtime_layer.asciidoc`:
     | {CL_sRGB}
     | {CL_RGB}
     | {CL_RGB}
  >> | {CL_sRGB}
     | {CL_sRGBx}
     | {CL_RGBx}
     | {CL_RGBx}
- `env/common_properties.asciidoc`:
     
     | 15
     | *sRGB*
  >> | `CL_sRGB`
     
     | 16
     | *sRGBx*

## `CL_sRGBA`  (container: `cl_device_info`, value: 0x10C1)
- `api/appendix_h.asciidoc`:
     
     == sRGB Images
     
  >> All of the sRGB image channel orders (such as {CL_sRGBA}) are optional for devices supporting OpenCL 3.0.
     When sRGB images are not supported:
     
     [cols="2,3",options="header",]
- `api/footnotes.asciidoc`:
     
     
     :fn-srgb-image-requirements: pass:n[ \
  >> Support for reading from the {CL_sRGBA} image channel order is optional for 1D image buffers. \
     Support for writing to the {CL_sRGBA} image channel order is optional for all image types. \
     ]
     
- `api/footnotes.asciidoc`:
     
     :fn-srgb-image-requirements: pass:n[ \
     Support for reading from the {CL_sRGBA} image channel order is optional for 1D image buffers. \
  >> Support for writing to the {CL_sRGBA} image channel order is optional for all image types. \
     ]
     
     :fn-thread-safe: pass:n[ \
- `api/opencl_runtime_layer.asciidoc`:
     
     [version-note]
     | A three channel image format, where the three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
  >> | {CL_sRGBA_anchor}, {CL_sBGRA_anchor}
     
     // The CL_sRGBA annotation here is used to convey the same information for both
     // entries in this table row.
- `api/opencl_runtime_layer.asciidoc`:
     | A three channel image format, where the three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
     | {CL_sRGBA_anchor}, {CL_sBGRA_anchor}
     
  >> // The CL_sRGBA annotation here is used to convey the same information for both
     // entries in this table row.
     [version-note]
     | Four channel image formats, where the first three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
- `api/opencl_runtime_layer.asciidoc`:
     
     // The CL_sRGBA annotation here is used to convey the same information for both
     // entries in this table row.
  >> [version-note]
     | Four channel image formats, where the first three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
     The fourth channel represents an `ALPHA` component.
     | {CL_sRGBx_anchor}

## `CL_sRGBx`  (container: `cl_device_info`, value: 0x10C0)
- `api/opencl_runtime_layer.asciidoc`:
     [version-note]
     | Four channel image formats, where the first three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
     The fourth channel represents an `ALPHA` component.
  >> | {CL_sRGBx_anchor}
     
     [version-note]
     | A four channel image format, where the three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
- `api/opencl_runtime_layer.asciidoc`:
     The fourth channel represents an `ALPHA` component.
     | {CL_sRGBx_anchor}
     
  >> [version-note]
     | A four channel image format, where the three channels represent `RED`, `GREEN`, and `BLUE` components in the sRGB color space.
     The fourth channel is ignored.
     |====
- `api/opencl_runtime_layer.asciidoc`:
     | {CL_RGB}
     | {CL_RGB}
     | {CL_sRGB}
  >> | {CL_sRGBx}
     | {CL_RGBx}
     | {CL_RGBx}
     | {CL_sRGBx}
- `api/opencl_runtime_layer.asciidoc`:
     | {CL_sRGBx}
     | {CL_RGBx}
     | {CL_RGBx}
  >> | {CL_sRGBx}
     | {CL_DEPTH}
     | {CL_R}
     |====
- `env/common_properties.asciidoc`:
     
     | 16
     | *sRGBx*
  >> | `CL_sRGBx`
     
     | 17
     | *sRGBA*

## `CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE`  (container: `enums.2000`, value: 0x2033)
- `api/appendix_e.asciidoc`:
     * {CL_PROGRAM_IL} to table 5.17 of the API specification.
     * {CL_QUEUE_DEVICE_DEFAULT} added to table 5.2 of the API specification.
     * Added table 5.22 to the API specification with the enums:
  >> {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE},
     {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE} and
     {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT}
     
- `api/appendix_h.asciidoc`:
     
     | {clGetKernelSubGroupInfo}
     | Returns {CL_INVALID_OPERATION} if _device_ does not support sub-groups.
  >> // Note: for {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE}, {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE},
     //       {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT}, {CL_KERNEL_MAX_NUM_SUB_GROUPS},
     //       {CL_KERNEL_COMPILE_NUM_SUB_GROUPS}.
     
- `api/opencl_runtime_layer.asciidoc`:
     [width="100%",cols="<25%,<25%,<25%,<25%",options="header"]
     |====
     | Kernel Sub-group Info | Input Type | Return Type | Description
  >> | {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE_anchor}
     
     [version-note]
     
- `api/opencl_runtime_layer.asciidoc`:
     | Kernel Sub-group Info | Input Type | Return Type | Description
     | {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_subgroups[]
     The equivalent {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE_KHR_anchor} may be used if
- `api/opencl_runtime_layer.asciidoc`:
     <<kernel-sub-group-info-table, Kernel Object Sub-group Queries>> table
     and _param_value_ is not `NULL`.
     * {CL_INVALID_VALUE} if _param_name_ is
  >> {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE},
     {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE} or
     {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT} and the size in bytes specified
     by _input_value_size_ is not valid or if _input_value_ is `NULL`.

## `CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE`  (container: `enums.2000`, value: 0x2034)
- `api/appendix_e.asciidoc`:
     * {CL_QUEUE_DEVICE_DEFAULT} added to table 5.2 of the API specification.
     * Added table 5.22 to the API specification with the enums:
     {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE},
  >> {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE} and
     {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT}
     
     The following modifications are made to the OpenCL 2.1 platform layer and
- `api/appendix_h.asciidoc`:
     
     | {clGetKernelSubGroupInfo}
     | Returns {CL_INVALID_OPERATION} if _device_ does not support sub-groups.
  >> // Note: for {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE}, {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE},
     //       {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT}, {CL_KERNEL_MAX_NUM_SUB_GROUPS},
     //       {CL_KERNEL_COMPILE_NUM_SUB_GROUPS}.
     
- `api/opencl_runtime_layer.asciidoc`:
     dispatch.
     The number of dimensions in the ND-range will be inferred from
     the value specified for _input_value_size_.
  >> | {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE_anchor}
     
     [version-note]
     
- `api/opencl_runtime_layer.asciidoc`:
     the value specified for _input_value_size_.
     | {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE_anchor}
     
  >> [version-note]
     
     ifdef::cl_khr_subgroups[]
     The equivalent {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE_KHR_anchor} may be used if
- `api/opencl_runtime_layer.asciidoc`:
     and _param_value_ is not `NULL`.
     * {CL_INVALID_VALUE} if _param_name_ is
     {CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE},
  >> {CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE} or
     {CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT} and the size in bytes specified
     by _input_value_size_ is not valid or if _input_value_ is `NULL`.
     * {CL_OUT_OF_RESOURCES} if there is a failure to allocate resources required

## `CL_SVM_ALLOC_ACCESS_FLAGS_KHR`  (container: `enums.2000`, value: 0x2079)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SVM_ALLOC_ALIGNMENT_KHR`  (container: `enums.2000`, value: 0x207A)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SVM_ALLOC_ASSOCIATED_DEVICE_HANDLE_KHR`  (container: `enums.2000`, value: 0x2078)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SVM_INFO_ACCESS_FLAGS_KHR`  (container: `enums.2000`, value: 0x208B)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SVM_INFO_CAPABILITIES_KHR`  (container: `enums.2000`, value: 0x2089)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SVM_INFO_PROPERTIES_KHR`  (container: `enums.2000`, value: 0x208A)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SVM_INFO_TYPE_INDEX_KHR`  (container: `enums.2000`, value: 0x2088)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_COMPUTE_CAPABILITY_MAJOR_NV`  (container: `enums.4000`, value: 0x4000)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_COMPUTE_CAPABILITY_MINOR_NV`  (container: `enums.4000`, value: 0x4001)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_GPU_OVERLAP_NV`  (container: `enums.4000`, value: 0x4004)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_INTEGRATED_MEMORY_NV`  (container: `enums.4000`, value: 0x4006)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_KERNEL_EXEC_TIMEOUT_NV`  (container: `enums.4000`, value: 0x4005)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_REGISTERS_PER_BLOCK_NV`  (container: `enums.4000`, value: 0x4002)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_WARP_SIZE_NV`  (container: `enums.4000`, value: 0x4003)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_ALL_DEVICES_FOR_DX9_INTEL`  (container: `enums.4010`, value: 0x4025)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_ACQUIRE_D3D9_OBJECTS_INTEL`  (container: `enums.4010`, value: 0x402A)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_ACQUIRE_DX9_OBJECTS_INTEL`  (container: `enums.4010`, value: 0x402A)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_RELEASE_D3D9_OBJECTS_INTEL`  (container: `enums.4010`, value: 0x402B)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_RELEASE_DX9_OBJECTS_INTEL`  (container: `enums.4010`, value: 0x402B)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_CONTEXT_D3D9_DEVICE_INTEL`  (container: `enums.4010`, value: 0x4026)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_D3D9_DEVICE_INTEL`  (container: `enums.4010`, value: 0x4022)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_DX9_RESOURCE_INTEL`  (container: `enums.4010`, value: 0x4027)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_PREFERRED_DEVICES_FOR_DX9_INTEL`  (container: `enums.4010`, value: 0x4024)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_BOARD_NAME_AMD`  (container: `enums.4030`, value: 0x4038)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_GLOBAL_FREE_MEMORY_AMD`  (container: `enums.4030`, value: 0x4039)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_MAX_WORK_GROUP_SIZE_AMD`  (container: `enums.4030`, value: 0x4031)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PCIE_ID_AMD`  (container: `enums.4030`, value: 0x4034)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PREFERRED_CONSTANT_BUFFER_SIZE_AMD`  (container: `enums.4030`, value: 0x4033)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PREFERRED_WORK_GROUP_SIZE_AMD`  (container: `enums.4030`, value: 0x4030)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PROFILING_TIMER_OFFSET_AMD`  (container: `enums.4030`, value: 0x4036)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_TOPOLOGY_AMD`  (container: `enums.4030`, value: 0x4037)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_MIGRATE_MEM_OBJECT_EXT`  (container: `enums.4040`, value: 0x4040)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_AVAILABLE_ASYNC_QUEUES_AMD`  (container: `enums.4040`, value: 0x404C)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_GFXIP_MAJOR_AMD`  (container: `enums.4040`, value: 0x404A)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_GFXIP_MINOR_AMD`  (container: `enums.4040`, value: 0x404B)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_GLOBAL_MEM_CHANNELS_AMD`  (container: `enums.4040`, value: 0x4044)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_GLOBAL_MEM_CHANNEL_BANKS_AMD`  (container: `enums.4040`, value: 0x4045)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_GLOBAL_MEM_CHANNEL_BANK_WIDTH_AMD`  (container: `enums.4040`, value: 0x4046)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_LOCAL_MEM_BANKS_AMD`  (container: `enums.4040`, value: 0x4048)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_LOCAL_MEM_SIZE_PER_COMPUTE_UNIT_AMD`  (container: `enums.4040`, value: 0x4047)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_SIMD_INSTRUCTION_WIDTH_AMD`  (container: `enums.4040`, value: 0x4042)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_SIMD_PER_COMPUTE_UNIT_AMD`  (container: `enums.4040`, value: 0x4040)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_SIMD_WIDTH_AMD`  (container: `enums.4040`, value: 0x4041)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_THREAD_TRACE_SUPPORTED_AMD`  (container: `enums.4040`, value: 0x4049)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_WAVEFRONT_WIDTH_AMD`  (container: `enums.4040`, value: 0x4043)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_AFFINITY_DOMAINS_EXT`  (container: `enums.4050`, value: 0x4056)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PARENT_DEVICE_EXT`  (container: `enums.4050`, value: 0x4054)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PARTITION_BY_AFFINITY_DOMAIN_EXT`  (container: `enums.4050`, value: 0x4053)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PARTITION_BY_COUNTS_EXT`  (container: `enums.4050`, value: 0x4051)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PARTITION_BY_NAMES_EXT`  (container: `enums.4050`, value: 0x4052)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PARTITION_BY_NAMES_INTEL`  (container: `enums.4050`, value: 0x4052)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PARTITION_EQUALLY_EXT`  (container: `enums.4050`, value: 0x4050)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PARTITION_STYLE_EXT`  (container: `enums.4050`, value: 0x4058)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PARTITION_TYPES_EXT`  (container: `enums.4050`, value: 0x4055)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_REFERENCE_COUNT_EXT`  (container: `enums.4050`, value: 0x4057)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_CONTEXT_D3D9EX_DEVICE_INTEL`  (container: `enums.4070`, value: 0x4072)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_CONTEXT_DXVA_DEVICE_INTEL`  (container: `enums.4070`, value: 0x4073)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_D3D9EX_DEVICE_INTEL`  (container: `enums.4070`, value: 0x4070)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_ME_VERSION_INTEL`  (container: `enums.4070`, value: 0x407E)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DXVA_DEVICE_INTEL`  (container: `enums.4070`, value: 0x4071)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMAGE_DX9_PLANE_INTEL`  (container: `enums.4070`, value: 0x4075)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_DX9_SHARED_HANDLE_INTEL`  (container: `enums.4070`, value: 0x4074)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_UYVY_INTEL`  (container: `enums.4070`, value: 0x4077)
- `extensions/cl_intel_packed_yuv.asciidoc`:
     [source]
     ----
     #define CL_YUYV_INTEL                               0x4076
  >> #define CL_UYVY_INTEL                               0x4077
     #define CL_YVYU_INTEL                               0x4078
     #define CL_VYUY_INTEL                               0x4079
     ----
- `extensions/cl_intel_packed_yuv.asciidoc`:
     [width="100%",cols="<50%,<50%",options="header"]
     |====
     | Image Channel Order | Description
  >> | `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, `CL_VYUY_INTEL`
     | Packed YUV image format.  This format can only be used if `image_channel_data_type` = `CL_UNORM_INT8`.
     |====
     --
- `extensions/cl_intel_packed_yuv.asciidoc`:
     | ...
     |====
     
  >> The memory layout of a packed YUV image when `image_channel_order` is `CL_UYVY_INTEL` is:
     
     [width="80%",cols="<20%,<20%,<20%,<20%,<20%"]
     |====
- `extensions/cl_intel_packed_yuv.asciidoc`:
     | `CL_YUYV_INTEL`
     | `CL_UNORM_INT8`
     | 2
  >> | `CL_UYVY_INTEL`
     | `CL_UNORM_INT8`
     | 2
     | `CL_YVYU_INTEL`
- `extensions/cl_intel_packed_yuv.asciidoc`:
     In section 6.15.15.1.1 Determining the border color or value, add a bullet for packed YUV formats: ::
     +
     --
  >> * If image channel order is `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, or `CL_VYUY_INTEL`, the border color is value is undefined.
     --
     
     Add to the un-numbered table in section 6.15.15.7 Mapping image channels to color values returned by read_image and color values passed to write_image
- `extensions/cl_intel_packed_yuv.asciidoc`:
     [cols=",",]
     |====
     | *Channel Order*   | `float4`, `int4` or `uint4` *components of channel data*
  >> | `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, `CL_VYUY_INTEL`
     | (V, Y, U, 1.0)
     |====
     --

## `CL_VYUY_INTEL`  (container: `enums.4070`, value: 0x4079)
- `extensions/cl_intel_packed_yuv.asciidoc`:
     #define CL_YUYV_INTEL                               0x4076
     #define CL_UYVY_INTEL                               0x4077
     #define CL_YVYU_INTEL                               0x4078
  >> #define CL_VYUY_INTEL                               0x4079
     ----
     
     == Modifications to the OpenCL API Specification
- `extensions/cl_intel_packed_yuv.asciidoc`:
     [width="100%",cols="<50%,<50%",options="header"]
     |====
     | Image Channel Order | Description
  >> | `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, `CL_VYUY_INTEL`
     | Packed YUV image format.  This format can only be used if `image_channel_data_type` = `CL_UNORM_INT8`.
     |====
     --
- `extensions/cl_intel_packed_yuv.asciidoc`:
     | ...
     |====
     
  >> The memory layout of a packed YUV image when `image_channel_order` is `CL_VYUY_INTEL` is:
     
     [width="80%",cols="<20%,<20%,<20%,<20%,<20%"]
     |====
- `extensions/cl_intel_packed_yuv.asciidoc`:
     | `CL_YVYU_INTEL`
     | `CL_UNORM_INT8`
     | 2
  >> | `CL_VYUY_INTEL`
     | `CL_UNORM_INT8`
     |====
     --
- `extensions/cl_intel_packed_yuv.asciidoc`:
     In section 6.15.15.1.1 Determining the border color or value, add a bullet for packed YUV formats: ::
     +
     --
  >> * If image channel order is `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, or `CL_VYUY_INTEL`, the border color is value is undefined.
     --
     
     Add to the un-numbered table in section 6.15.15.7 Mapping image channels to color values returned by read_image and color values passed to write_image
- `extensions/cl_intel_packed_yuv.asciidoc`:
     [cols=",",]
     |====
     | *Channel Order*   | `float4`, `int4` or `uint4` *components of channel data*
  >> | `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, `CL_VYUY_INTEL`
     | (V, Y, U, 1.0)
     |====
     --

## `CL_YUYV_INTEL`  (container: `enums.4070`, value: 0x4076)
- `extensions/cl_intel_packed_yuv.asciidoc`:
     
     [source]
     ----
  >> #define CL_YUYV_INTEL                               0x4076
     #define CL_UYVY_INTEL                               0x4077
     #define CL_YVYU_INTEL                               0x4078
     #define CL_VYUY_INTEL                               0x4079
- `extensions/cl_intel_packed_yuv.asciidoc`:
     [width="100%",cols="<50%,<50%",options="header"]
     |====
     | Image Channel Order | Description
  >> | `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, `CL_VYUY_INTEL`
     | Packed YUV image format.  This format can only be used if `image_channel_data_type` = `CL_UNORM_INT8`.
     |====
     --
- `extensions/cl_intel_packed_yuv.asciidoc`:
     --
     The only supported `image_channel_data_type` for packed YUV images is `CL_UNORM_INT8`.
     
  >> The memory layout of a packed YUV image when `image_channel_order` is `CL_YUYV_INTEL` is:
     
     [width="80%",cols="<20%,<20%,<20%,<20%,<20%"]
     |====
- `extensions/cl_intel_packed_yuv.asciidoc`:
     |====
     | num_channels | channel_order | channel_data_type
     | 2
  >> | `CL_YUYV_INTEL`
     | `CL_UNORM_INT8`
     | 2
     | `CL_UYVY_INTEL`
- `extensions/cl_intel_packed_yuv.asciidoc`:
     In section 6.15.15.1.1 Determining the border color or value, add a bullet for packed YUV formats: ::
     +
     --
  >> * If image channel order is `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, or `CL_VYUY_INTEL`, the border color is value is undefined.
     --
     
     Add to the un-numbered table in section 6.15.15.7 Mapping image channels to color values returned by read_image and color values passed to write_image
- `extensions/cl_intel_packed_yuv.asciidoc`:
     [cols=",",]
     |====
     | *Channel Order*   | `float4`, `int4` or `uint4` *components of channel data*
  >> | `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, `CL_VYUY_INTEL`
     | (V, Y, U, 1.0)
     |====
     --

## `CL_YVYU_INTEL`  (container: `enums.4070`, value: 0x4078)
- `extensions/cl_intel_packed_yuv.asciidoc`:
     ----
     #define CL_YUYV_INTEL                               0x4076
     #define CL_UYVY_INTEL                               0x4077
  >> #define CL_YVYU_INTEL                               0x4078
     #define CL_VYUY_INTEL                               0x4079
     ----
     
- `extensions/cl_intel_packed_yuv.asciidoc`:
     [width="100%",cols="<50%,<50%",options="header"]
     |====
     | Image Channel Order | Description
  >> | `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, `CL_VYUY_INTEL`
     | Packed YUV image format.  This format can only be used if `image_channel_data_type` = `CL_UNORM_INT8`.
     |====
     --
- `extensions/cl_intel_packed_yuv.asciidoc`:
     | ...
     |====
     
  >> The memory layout of a packed YUV image when `image_channel_order` is `CL_YVYU_INTEL` is:
     
     [width="80%",cols="<20%,<20%,<20%,<20%,<20%"]
     |====
- `extensions/cl_intel_packed_yuv.asciidoc`:
     | `CL_UYVY_INTEL`
     | `CL_UNORM_INT8`
     | 2
  >> | `CL_YVYU_INTEL`
     | `CL_UNORM_INT8`
     | 2
     | `CL_VYUY_INTEL`
- `extensions/cl_intel_packed_yuv.asciidoc`:
     In section 6.15.15.1.1 Determining the border color or value, add a bullet for packed YUV formats: ::
     +
     --
  >> * If image channel order is `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, or `CL_VYUY_INTEL`, the border color is value is undefined.
     --
     
     Add to the un-numbered table in section 6.15.15.7 Mapping image channels to color values returned by read_image and color values passed to write_image
- `extensions/cl_intel_packed_yuv.asciidoc`:
     [cols=",",]
     |====
     | *Channel Order*   | `float4`, `int4` or `uint4` *components of channel data*
  >> | `CL_YUYV_INTEL`, `CL_UYVY_INTEL`, `CL_YVYU_INTEL`, `CL_VYUY_INTEL`
     | (V, Y, U, 1.0)
     |====
     --

## `CL_ACCELERATOR_CONTEXT_INTEL`  (container: `enums.4090`, value: 0x4092)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_ACCELERATOR_DESCRIPTOR_INTEL`  (container: `enums.4090`, value: 0x4090)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_ACCELERATOR_REFERENCE_COUNT_INTEL`  (container: `enums.4090`, value: 0x4091)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_ACCELERATOR_TYPE_INTEL`  (container: `enums.4090`, value: 0x4093)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_ALL_DEVICES_FOR_VA_API_INTEL`  (container: `enums.4090`, value: 0x4096)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_ACQUIRE_VA_API_MEDIA_SURFACES_INTEL`  (container: `enums.4090`, value: 0x409A)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_RELEASE_VA_API_MEDIA_SURFACES_INTEL`  (container: `enums.4090`, value: 0x409B)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_CONTEXT_VA_API_DISPLAY_INTEL`  (container: `enums.4090`, value: 0x4097)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMAGE_VA_API_PLANE_INTEL`  (container: `enums.4090`, value: 0x4099)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_VA_API_MEDIA_SURFACE_INTEL`  (container: `enums.4090`, value: 0x4098)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_PREFERRED_DEVICES_FOR_VA_API_INTEL`  (container: `enums.4090`, value: 0x4095)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_VA_API_DISPLAY_INTEL`  (container: `enums.4090`, value: 0x4094)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_EXT_MEM_PADDING_IN_BYTES_QCOM`  (container: `enums.40A0`, value: 0x40A0)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_PAGE_SIZE_QCOM`  (container: `enums.40A0`, value: 0x40A1)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMAGE_ROW_ALIGNMENT_QCOM`  (container: `enums.40A0`, value: 0x40A2)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMAGE_SLICE_ALIGNMENT_QCOM`  (container: `enums.40A0`, value: 0x40A3)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_HOST_IOCOHERENT_QCOM`  (container: `enums.40A0`, value: 0x40A9)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_HOST_UNCACHED_QCOM`  (container: `enums.40A0`, value: 0x40A4)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_HOST_WRITEBACK_QCOM`  (container: `enums.40A0`, value: 0x40A5)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_HOST_WRITETHROUGH_QCOM`  (container: `enums.40A0`, value: 0x40A6)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_HOST_WRITE_COMBINING_QCOM`  (container: `enums.40A0`, value: 0x40A7)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_ION_HOST_PTR_QCOM`  (container: `enums.40A0`, value: 0x40A8)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_SVM_FREE_ARM`  (container: `enums.40B0`, value: 0x40BA)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_SVM_MAP_ARM`  (container: `enums.40B0`, value: 0x40BD)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_SVM_MEMCPY_ARM`  (container: `enums.40B0`, value: 0x40BB)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_SVM_MEMFILL_ARM`  (container: `enums.40B0`, value: 0x40BC)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_SVM_UNMAP_ARM`  (container: `enums.40B0`, value: 0x40BE)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_COMPUTE_UNITS_BITFIELD_ARM`  (container: `enums.40B0`, value: 0x40BF)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_SVM_CAPABILITIES_ARM`  (container: `enums.40B0`, value: 0x40B6)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMPORT_TYPE_ARM`  (container: `enums.40B0`, value: 0x40B2)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMPORT_TYPE_DMA_BUF_ARM`  (container: `enums.40B0`, value: 0x40B4)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMPORT_TYPE_HOST_ARM`  (container: `enums.40B0`, value: 0x40B3)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMPORT_TYPE_PROTECTED_ARM`  (container: `enums.40B0`, value: 0x40B5)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM_ARM`  (container: `enums.40B0`, value: 0x40B9)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_KERNEL_EXEC_INFO_SVM_PTRS_ARM`  (container: `enums.40B0`, value: 0x40B8)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_USES_SVM_POINTER_ARM`  (container: `enums.40B0`, value: 0x40B7)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_PRINTF_BUFFERSIZE_ARM`  (container: `enums.40B0`, value: 0x40B1)
- `extensions/cl_arm_printf.asciidoc`:
     [source,c]
     ----
     CL_PRINTF_CALLBACK_ARM    0x40B0
  >> CL_PRINTF_BUFFERSIZE_ARM  0x40B1
     ----
     
     == New OpenCL C Functions
- `extensions/cl_arm_printf.asciidoc`:
     If this property is not specified, no callback will be registered and any printf output from
     a kernel will be discarded.
     
  >> | `CL_PRINTF_BUFFERSIZE_ARM`
     | `size_t`
     | Specifies the size of printf buffer allocations to use within the driver.
     A printf buffer is allocated per device per context, within a context the buffer
- `extensions/cl_arm_printf.asciidoc`:
     
     /* Request a minimum printf buffer size of 4MiB for devices in the
     context that support this extension. */
  >> CL_PRINTF_BUFFERSIZE_ARM, (cl_context_properties) 0x100000,
     
     CL_CONTEXT_PLATFORM,      (cl_context_properties) platform,
     0

## `CL_PRINTF_CALLBACK_ARM`  (container: `enums.40B0`, value: 0x40B0)
- `extensions/cl_arm_printf.asciidoc`:
     
     [source,c]
     ----
  >> CL_PRINTF_CALLBACK_ARM    0x40B0
     CL_PRINTF_BUFFERSIZE_ARM  0x40B1
     ----
     
- `extensions/cl_arm_printf.asciidoc`:
     | Property value
     | Description
     
  >> | `CL_PRINTF_CALLBACK_ARM`
     | `(void)(*callback)(const char *buffer, size_t len, size_t complete, void *user_data)`
     | Specifies a pointer to function to be invoked when printf data is available.
     Upon invocation the arguments are set to the following values: +
- `extensions/cl_arm_printf.asciidoc`:
     cl_context_properties properties[] =
     {
     /* Enable a printf callback function for this context. */
  >> CL_PRINTF_CALLBACK_ARM,   (cl_context_properties) printf_callback,
     
     /* Request a minimum printf buffer size of 4MiB for devices in the
     context that support this extension. */

## `CL_MEM_ANDROID_NATIVE_BUFFER_HOST_PTR_QCOM`  (container: `enums.40C0`, value: 0x40C6)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_PERF_HINT_HIGH_QCOM`  (container: `enums.40C0`, value: 0x40C3)
- `extensions/cl_qcom_perf_hint.asciidoc`:
     
     [source,c]
     ----
  >> #define CL_PERF_HINT_HIGH_QCOM       0x40C3
     #define CL_PERF_HINT_NORMAL_QCOM     0x40C4
     #define CL_PERF_HINT_LOW_QCOM        0x40C5
     ----
- `extensions/cl_qcom_perf_hint.asciidoc`:
     | `cl_perf_hint_qcom`
     | Description
     
  >> | `CL_PERF_HINT_HIGH_QCOM`
     | Requests the highest performance level from device. This is the default setting for devices in an OpenCL context.
     | `CL_PERF_HINT_NORMAL_QCOM`
     | Requests a balanced performance setting that is set dynamically by the GPU frequency and power management.

## `CL_PERF_HINT_LOW_QCOM`  (container: `enums.40C0`, value: 0x40C5)
- `extensions/cl_qcom_perf_hint.asciidoc`:
     ----
     #define CL_PERF_HINT_HIGH_QCOM       0x40C3
     #define CL_PERF_HINT_NORMAL_QCOM     0x40C4
  >> #define CL_PERF_HINT_LOW_QCOM        0x40C5
     ----
     
     
- `extensions/cl_qcom_perf_hint.asciidoc`:
     | Requests the highest performance level from device. This is the default setting for devices in an OpenCL context.
     | `CL_PERF_HINT_NORMAL_QCOM`
     | Requests a balanced performance setting that is set dynamically by the GPU frequency and power management.
  >> | `CL_PERF_HINT_LOW_QCOM`
     | Requests a performance setting that prioritizes lower power consumption
     
     |====
- `extensions/cl_qcom_perf_hint.asciidoc`:
     [source,c]
     
     cl_context_properties properties[] = {CL_CONTEXT_PERF_HINT_QCOM,
  >> CL_PERF_HINT_LOW_QCOM, 0};
     clCreateContext(properties, 1, &device_id, NULL, NULL, NULL);
     
     2) Set performance hint for an existing CL context:

## `CL_PERF_HINT_NORMAL_QCOM`  (container: `enums.40C0`, value: 0x40C4)
- `extensions/cl_qcom_perf_hint.asciidoc`:
     [source,c]
     ----
     #define CL_PERF_HINT_HIGH_QCOM       0x40C3
  >> #define CL_PERF_HINT_NORMAL_QCOM     0x40C4
     #define CL_PERF_HINT_LOW_QCOM        0x40C5
     ----
     
- `extensions/cl_qcom_perf_hint.asciidoc`:
     
     | `CL_PERF_HINT_HIGH_QCOM`
     | Requests the highest performance level from device. This is the default setting for devices in an OpenCL context.
  >> | `CL_PERF_HINT_NORMAL_QCOM`
     | Requests a balanced performance setting that is set dynamically by the GPU frequency and power management.
     | `CL_PERF_HINT_LOW_QCOM`
     | Requests a performance setting that prioritizes lower power consumption
- `extensions/cl_qcom_perf_hint.asciidoc`:
     
     [source,c]
     
  >> clSetPerfHintQCOM(context, CL_PERF_HINT_NORMAL_QCOM);
     
     
     == Version History

## `CL_COMMAND_ACQUIRE_GRALLOC_OBJECTS_IMG`  (container: `enums.40D0`, value: 0x40D2)
- `extensions/cl_img_use_gralloc_ptr.asciidoc`:
     
     [source,c]
     ----
  >> CL_COMMAND_ACQUIRE_GRALLOC_OBJECTS_IMG 0x40D2
     CL_COMMAND_RELEASE_GRALLOC_OBJECTS_IMG 0x40D3
     ----
     

## `CL_COMMAND_GENERATE_MIPMAP_IMG`  (container: `enums.40D0`, value: 0x40D6)
- `extensions/cl_img_generate_mipmap.asciidoc`:
     
     [source,c]
     ----
  >> CL_COMMAND_GENERATE_MIPMAP_IMG 0x40D6
     ----
     
     == New API Functions

## `CL_COMMAND_RELEASE_GRALLOC_OBJECTS_IMG`  (container: `enums.40D0`, value: 0x40D3)
- `extensions/cl_img_use_gralloc_ptr.asciidoc`:
     [source,c]
     ----
     CL_COMMAND_ACQUIRE_GRALLOC_OBJECTS_IMG 0x40D2
  >> CL_COMMAND_RELEASE_GRALLOC_OBJECTS_IMG 0x40D3
     ----
     
     New error codes:

## `CL_DEVICE_MEMORY_CAPABILITIES_IMG`  (container: `enums.40D0`, value: 0x40D8)
- `extensions/cl_img_mem_properties.asciidoc`:
     | Return Type
     | Description
     
  >> | `CL_DEVICE_MEMORY_CAPABILITIES_IMG`
     | `cl_mem_alloc_flags_img`
     | Allocation flags describing the memory region capabilities by the device.
     |====

## `CL_DEVICE_SAFETY_MEM_SIZE_IMG`  (container: `enums.40D0`, value: 0x40DC)
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     ----
     #define CL_DEVICE_WORKGROUP_PROTECTION_SVM_CAPABILITIES_IMG            0x40DA
     #define CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG 0x40DB
  >> #define CL_DEVICE_SAFETY_MEM_SIZE_IMG                                  0x40DC
     ----
     
     Additional values that can be returned in _param_value_ when *clGetEventInfo* is called with `CL_EVENT_COMMAND_EXECUTION_STATUS` given as _param_name_
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     
     Devices that set `CL_DEVICE_QUEUE_SUPPORTED` for `CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG` must also return `CL_TRUE` for `CL_D
     
  >> |`CL_DEVICE_SAFETY_MEM_SIZE_IMG`
     
     |`cl_ulong`
     
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     |====
     | Version | Date       | Author             | Changes
     | 1.0.0   | 2025-07-08 | Ahmed Amrani Akdi  | *Updated to 1.0.0 version for publishing.*
  >> | 0.6.0   | 2025-05-02 | Ahmed Amrani Akdi  | *Added `CL_DEVICE_SAFETY_MEM_SIZE_IMG`*
     | 0.5.0   | 2022-01-17 | Jeremy Kemp        | *Added `CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG`*
     | 0.4.0   | 2020-12-03 | Jeremy Kemp        | *Added event execution status as extension. Tidy up*
     | 0.3.0   | 2020-11-25 | Jeremy Kemp        | *Added SVM queries. Added new event status codes. Lots of additional updates and fixes*

## `CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG`  (container: `enums.40D0`, value: 0x40DB)
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     [source,c]
     ----
     #define CL_DEVICE_WORKGROUP_PROTECTION_SVM_CAPABILITIES_IMG            0x40DA
  >> #define CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG 0x40DB
     #define CL_DEVICE_SAFETY_MEM_SIZE_IMG                                  0x40DC
     ----
     
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     
     For other device versions there is no mandated minimum capability.
     
  >> |`CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG`
     
     |`cl_device_device_enqueue_capabilities`
     | May return 0, indicating that device does not support device-side enqueue and on-device queues when operating with workgroup protection enabled. Oth
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     
     If `CL_DEVICE_QUEUE_REPLACEABLE_DEFAULT` is set, `CL_DEVICE_QUEUE_SUPPORTED` must also be set.
     
  >> Devices that set `CL_DEVICE_QUEUE_SUPPORTED` for `CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG` must also return `CL_TRUE` for `CL_D
     
     |`CL_DEVICE_SAFETY_MEM_SIZE_IMG`
     
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     | Version | Date       | Author             | Changes
     | 1.0.0   | 2025-07-08 | Ahmed Amrani Akdi  | *Updated to 1.0.0 version for publishing.*
     | 0.6.0   | 2025-05-02 | Ahmed Amrani Akdi  | *Added `CL_DEVICE_SAFETY_MEM_SIZE_IMG`*
  >> | 0.5.0   | 2022-01-17 | Jeremy Kemp        | *Added `CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG`*
     | 0.4.0   | 2020-12-03 | Jeremy Kemp        | *Added event execution status as extension. Tidy up*
     | 0.3.0   | 2020-11-25 | Jeremy Kemp        | *Added SVM queries. Added new event status codes. Lots of additional updates and fixes*
     | 0.2.1   | 2020-11-06 | Jeremy Kemp        | *Resolved Issue 3. Removed `cl_arm_import_memory` restriction*

## `CL_DEVICE_WORKGROUP_PROTECTION_SVM_CAPABILITIES_IMG`  (container: `enums.40D0`, value: 0x40DA)
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     Additional _param_name_ values that can be passed to `clGetDeviceInfo`:
     [source,c]
     ----
  >> #define CL_DEVICE_WORKGROUP_PROTECTION_SVM_CAPABILITIES_IMG            0x40DA
     #define CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG 0x40DB
     #define CL_DEVICE_SAFETY_MEM_SIZE_IMG                                  0x40DC
     ----
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     | Return Type
     | Description
     
  >> | `CL_DEVICE_WORKGROUP_PROTECTION_SVM_CAPABILITIES_IMG`
     Missing before version 2.0.
     | `cl_device_svm_capabilities`
     

## `CL_ECC_RECOVERED_IMG`  (container: `enums.40D0`, value: 0x40DD)
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     
     [source,c]
     ----
  >> #define CL_ECC_RECOVERED_IMG   0x40DD
     #define CL_PAGE_FAULT_IMG      -1127
     #define CL_SAFETY_FAULT_IMG    -1128
     #define CL_GENERAL_FAULT_IMG   -1129
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     * `CL_PAGE_FAULT_IMG` This indicates that the command was present during execution that resulted in a page fault and is an error code. This status can
     * `CL_SAFETY_FAULT_IMG` This indicates that the command was present during execution that resulted in workgroup protection identifying an error with t
     * `CL_GENERAL_FAULT_IMG` This indicates that the command was present during execution that resulted in an error with the command and is an error code.
  >> * `CL_ECC_RECOVERED_IMG` This indicates that the command has successfully completed and is considered to have the same semantics as `CL_COMPLETE`. It 
     * `CL_ECC_UNRECOVERED_IMG` This indicates that the command was present during execution that resulted in an ECC event where memory was not successfull
     
     (Add the following to Table 36. List of supported param_names by clGetEventInfo) ::
- `extensions/cl_img_safety_mechanisms.asciidoc`:
     
     `CL_GENERAL_FAULT_IMG` (during execution, the command was present during a general fault and should be considered to have failed execution)
     
  >> `CL_ECC_RECOVERED_IMG` (during execution, the command was present during an ECC event where the memory successfully self-corrected. This can be consid
     
     `CL_ECC_UNRECOVERED_IMG` (during execution, the command was present during an ECC event where the memory did not successfully self-correct and should 
     |====

## `CL_GRALLOC_RESOURCE_NOT_ACQUIRED_IMG`  (container: `enums.40D0`, value: 0x40D4)
- `extensions/cl_img_use_gralloc_ptr.asciidoc`:
     
     [source,c]
     ----
  >> CL_GRALLOC_RESOURCE_NOT_ACQUIRED_IMG 0x40D4
     CL_INVALID_GRALLOC_OBJECT_IMG        0x40D5
     ----
     
- `extensions/cl_img_use_gralloc_ptr.asciidoc`:
     ----
     is used to acquire OpenCL memory objects that have been created from gralloc resources. The gralloc objects are acquired by the OpenCL context associa
     
  >> OpenCL memory objects created from gralloc resources must be acquired before they can be used by any OpenCL commands queued to a command-queue. If an 
     
     This function has no affect on memory objects in _mem_objects_ that have already been acquired, ignoring them silently. The function returns CL_SUCCES
     
- `extensions/cl_img_use_gralloc_ptr.asciidoc`:
     * `CL_INVALID_MEM_OBJECT` if memory objects in _mem_objects_ are not valid OpenCL memory objects in the context associated with _command_queue_.
     * `CL_INVALID_GRALLOC_OBJECT_IMG` if memory objects in _mem_objects_ have not been created from gralloc resources.
     * `CL_INVALID_COMMAND_QUEUE` if _command_queue_ is not a valid command-queue.
  >> * `CL_GRALLOC_RESOURCE_NOT_ACQUIRED_IMG` if memory objects in _mem_objects_ have not previously acquired with *clEnqueueAcquireGrallocObjectsIMG*, or 
     * `CL_INVALID_EVENT_WAIT_LIST` if _event_wait_list_ is NULL and _num_events_in_wait_list_ 0, or _event_wait_list_ is not `NULL` and _num_events_in_wai
     * `CL_OUT_OF_RESOURCES` if there is a failure to allocate resources required by the OpenCL implementation on the device.
     * `CL_OUT_OF_HOST_MEMORY` if there is a failure to allocate resources required by the OpenCL implementation on the host.

## `CL_INVALID_GRALLOC_OBJECT_IMG`  (container: `enums.40D0`, value: 0x40D5)
- `extensions/cl_img_use_gralloc_ptr.asciidoc`:
     [source,c]
     ----
     CL_GRALLOC_RESOURCE_NOT_ACQUIRED_IMG 0x40D4
  >> CL_INVALID_GRALLOC_OBJECT_IMG        0x40D5
     ----
     
     Accepted value for the _flags_ parameter to *clCreateBuffer* and *clCreateImage*:
- `extensions/cl_img_use_gralloc_ptr.asciidoc`:
     
     * `CL_INVALID_VALUE` if _num_objects_ is zero and _mem_objects_ is not a `NULL` value or if _num_objects_ 0 and _mem_objects_ is `NULL`.
     * `CL_INVALID_MEM_OBJECT` if memory objects in _mem_objects_ are not valid OpenCL memory objects in the context associated with _command_queue_.
  >> * `CL_INVALID_GRALLOC_OBJECT_IMG` if memory objects in _mem_objects_ have not been created from gralloc resources.
     * `CL_INVALID_COMMAND_QUEUE` if _command_queue_ is not a valid command-queue.
     * `CL_INVALID_EVENT_WAIT_LIST` if _event_wait_list_ is `NULL` and _num_events_in_wait_list_ 0, or _event_wait_list_ is not `NULL` and _num_events_in_w
     * `CL_OUT_OF_RESOURCES` if there is a failure to allocate resources required by the OpenCL implementation on the device.
- `extensions/cl_img_use_gralloc_ptr.asciidoc`:
     
     * `CL_INVALID_VALUE` if _num_objects_ is zero and _mem_objects_ is not a `NULL` value or if _num_objects_ 0 and _mem_objects_ is `NULL`.
     * `CL_INVALID_MEM_OBJECT` if memory objects in _mem_objects_ are not valid OpenCL memory objects in the context associated with _command_queue_.
  >> * `CL_INVALID_GRALLOC_OBJECT_IMG` if memory objects in _mem_objects_ have not been created from gralloc resources.
     * `CL_INVALID_COMMAND_QUEUE` if _command_queue_ is not a valid command-queue.
     * `CL_GRALLOC_RESOURCE_NOT_ACQUIRED_IMG` if memory objects in _mem_objects_ have not previously acquired with *clEnqueueAcquireGrallocObjectsIMG*, or 
     * `CL_INVALID_EVENT_WAIT_LIST` if _event_wait_list_ is NULL and _num_events_in_wait_list_ 0, or _event_wait_list_ is not `NULL` and _num_events_in_wai

## `CL_NV21`  (container: `enums.40D0`, value: 0x40D0)
- `extensions/cl_img_yuv_image.asciidoc`:
     | Version | Date       | Author       | Changes
     | 1.0.0   | 2020-11-10 | Jeremy Kemp  | Refreshed to AsciiDoc. Updated Contributors. Updated copyright notice. Updated the OpenCL spec which this exte
     | 0.3.0   | 2018-05-23 | GitHub User H1Gdev  | Remove duplicate 'for' in cl_img_yuv_image.txt.
  >> | 0.2.0   | 2017-10-17 | James Laverack & Robert Quill  | Replace CL_NV21 and CL_YV12 with CL_NV21_IMG and CL_YV12_IMG respectively.
     | 0.1.0   | 2014-05-02 | James Laverack  | Initial revision.
     |====
     

## `CL_NV21_IMG`  (container: `enums.40D0`, value: 0x40D0)
- `extensions/cl_img_yuv_image.asciidoc`:
     
     [source,c]
     ----
  >> CL_NV21_IMG 0x40D0
     CL_YV12_IMG 0x40D1
     ----
     
- `extensions/cl_img_yuv_image.asciidoc`:
     --
     
     (Add the following to return conditions to Section 5.3.1, _Creating Image Objects_) ::
  >> * `CL_INVALID_IMAGE_SIZE` if the _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and image dimensions specified in _image_desc_ are not suppor
     * `CL_INVALID_VALUE` if the _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the _image_desc_ is not `CL_MEM_OBJECT_IMAGE2D`.
     
     (Add the following to Table 16, _Image Format Descriptor_) ::
- `extensions/cl_img_yuv_image.asciidoc`:
     
     (Add the following to return conditions to Section 5.3.1, _Creating Image Objects_) ::
     * `CL_INVALID_IMAGE_SIZE` if the _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and image dimensions specified in _image_desc_ are not suppor
  >> * `CL_INVALID_VALUE` if the _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the _image_desc_ is not `CL_MEM_OBJECT_IMAGE2D`.
     
     (Add the following to Table 16, _Image Format Descriptor_) ::
     [cols="1,4",options="header"]
- `extensions/cl_img_yuv_image.asciidoc`:
     | Image Channel Order
     | Description
     
  >> | `CL_NV21_IMG, CL_YV12_IMG`
     | This format can only be used if _image_channel_data_type_ is `CL_UNORM_INT8`.
     |====
     
- `extensions/cl_img_yuv_image.asciidoc`:
     |====
     
     (Add the following to return conditions to Section 5.3.3, _Reading, Writing and Copying Image Objects_) ::
  >> * `CL_INVALID_VALUE` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the region is not the full size of the image and/or the origin is 
     
     (Add the following to return conditions to Section 5.3.4, _Filling Image Objects_) ::
     * `CL_IMAGE_FORMAT_NOT_SUPPORTED` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG`.
- `extensions/cl_img_yuv_image.asciidoc`:
     * `CL_INVALID_VALUE` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the region is not the full size of the image and/or the origin is 
     
     (Add the following to return conditions to Section 5.3.4, _Filling Image Objects_) ::
  >> * `CL_IMAGE_FORMAT_NOT_SUPPORTED` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG`.
     
     (Add the following to return conditions to Section 5.3.6, _Mapping Image Objects_) ::
     * `CL_INVALID_VALUE` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the region is not the full size of the image and/or the origin is 

## `CL_YV12`  (container: `enums.40D0`, value: 0x40D1)
- `extensions/cl_img_yuv_image.asciidoc`:
     | Version | Date       | Author       | Changes
     | 1.0.0   | 2020-11-10 | Jeremy Kemp  | Refreshed to AsciiDoc. Updated Contributors. Updated copyright notice. Updated the OpenCL spec which this exte
     | 0.3.0   | 2018-05-23 | GitHub User H1Gdev  | Remove duplicate 'for' in cl_img_yuv_image.txt.
  >> | 0.2.0   | 2017-10-17 | James Laverack & Robert Quill  | Replace CL_NV21 and CL_YV12 with CL_NV21_IMG and CL_YV12_IMG respectively.
     | 0.1.0   | 2014-05-02 | James Laverack  | Initial revision.
     |====
     

## `CL_YV12_IMG`  (container: `enums.40D0`, value: 0x40D1)
- `extensions/cl_img_yuv_image.asciidoc`:
     [source,c]
     ----
     CL_NV21_IMG 0x40D0
  >> CL_YV12_IMG 0x40D1
     ----
     
     == Modifications to the OpenCL API Specification
- `extensions/cl_img_yuv_image.asciidoc`:
     --
     
     (Add the following to return conditions to Section 5.3.1, _Creating Image Objects_) ::
  >> * `CL_INVALID_IMAGE_SIZE` if the _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and image dimensions specified in _image_desc_ are not suppor
     * `CL_INVALID_VALUE` if the _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the _image_desc_ is not `CL_MEM_OBJECT_IMAGE2D`.
     
     (Add the following to Table 16, _Image Format Descriptor_) ::
- `extensions/cl_img_yuv_image.asciidoc`:
     
     (Add the following to return conditions to Section 5.3.1, _Creating Image Objects_) ::
     * `CL_INVALID_IMAGE_SIZE` if the _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and image dimensions specified in _image_desc_ are not suppor
  >> * `CL_INVALID_VALUE` if the _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the _image_desc_ is not `CL_MEM_OBJECT_IMAGE2D`.
     
     (Add the following to Table 16, _Image Format Descriptor_) ::
     [cols="1,4",options="header"]
- `extensions/cl_img_yuv_image.asciidoc`:
     | Image Channel Order
     | Description
     
  >> | `CL_NV21_IMG, CL_YV12_IMG`
     | This format can only be used if _image_channel_data_type_ is `CL_UNORM_INT8`.
     |====
     
- `extensions/cl_img_yuv_image.asciidoc`:
     |====
     
     (Add the following to return conditions to Section 5.3.3, _Reading, Writing and Copying Image Objects_) ::
  >> * `CL_INVALID_VALUE` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the region is not the full size of the image and/or the origin is 
     
     (Add the following to return conditions to Section 5.3.4, _Filling Image Objects_) ::
     * `CL_IMAGE_FORMAT_NOT_SUPPORTED` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG`.
- `extensions/cl_img_yuv_image.asciidoc`:
     * `CL_INVALID_VALUE` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the region is not the full size of the image and/or the origin is 
     
     (Add the following to return conditions to Section 5.3.4, _Filling Image Objects_) ::
  >> * `CL_IMAGE_FORMAT_NOT_SUPPORTED` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG`.
     
     (Add the following to return conditions to Section 5.3.6, _Mapping Image Objects_) ::
     * `CL_INVALID_VALUE` if _image_channel_order_ is `CL_NV21_IMG` or `CL_YV12_IMG` and the region is not the full size of the image and/or the origin is 

## `CL_CONTEXT_SHOW_DIAGNOSTICS_INTEL`  (container: `enums.4100`, value: 0x4106)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_AVC_ME_SUPPORTS_PREEMPTION_INTEL`  (container: `enums.4100`, value: 0x410D)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_AVC_ME_SUPPORTS_TEXTURE_SAMPLER_USE_INTEL`  (container: `enums.4100`, value: 0x410C)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_AVC_ME_VERSION_INTEL`  (container: `enums.4100`, value: 0x410B)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_NUM_SIMULTANEOUS_INTEROPS_INTEL`  (container: `enums.4100`, value: 0x4105)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_SIMULTANEOUS_INTEROPS_INTEL`  (container: `enums.4100`, value: 0x4104)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_SUB_GROUP_SIZES_INTEL`  (container: `enums.4100`, value: 0x4108)
- `extensions/cl_intel_required_subgroup_size.asciidoc`:
     // C++ unless it is required.
     //:language: {basebackend@docbook:c++:cpp}
     
  >> :CL_DEVICE_SUB_GROUP_SIZES_INTEL: pass:q[`CL_&#8203;DEVICE_&#8203;SUB_&#8203;GROUP_&#8203;SIZES_&#8203;INTEL`]
     :CL_KERNEL_SPILL_MEM_SIZE_INTEL: pass:q[`CL_&#8203;KERNEL_&#8203;SPILL_&#8203;MEM_&#8203;SIZE_&#8203;INTEL`]
     :CL_KERNEL_COMPILE_SUB_GROUP_SIZE_INTEL: pass:q[`CL_&#8203;KERNEL_&#8203;COMPILE_&#8203;SUB_&#8203;GROUP_&#8203;SIZE_&#8203;INTEL`]
     
- `extensions/cl_intel_required_subgroup_size.asciidoc`:
     
     [source]
     ----
  >> CL_DEVICE_SUB_GROUP_SIZES_INTEL                 0x4108
     ----
     
     Accepted as the _param_name_ parameter of *clGetKernelWorkGroupInfo*:
- `extensions/cl_intel_required_subgroup_size.asciidoc`:
     |====
     | *cl_device_info* | Return Type | Description
     
  >> | {CL_DEVICE_SUB_GROUP_SIZES_INTEL}
     | `size_t[]`
     | Returns the set of sub-group sizes supported by the device.
     

## `CL_EGL_YUV_PLANE_INTEL`  (container: `enums.4100`, value: 0x4107)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_KERNEL_COMPILE_SUB_GROUP_SIZE_INTEL`  (container: `enums.4100`, value: 0x410A)
- `extensions/cl_intel_required_subgroup_size.asciidoc`:
     
     :CL_DEVICE_SUB_GROUP_SIZES_INTEL: pass:q[`CL_&#8203;DEVICE_&#8203;SUB_&#8203;GROUP_&#8203;SIZES_&#8203;INTEL`]
     :CL_KERNEL_SPILL_MEM_SIZE_INTEL: pass:q[`CL_&#8203;KERNEL_&#8203;SPILL_&#8203;MEM_&#8203;SIZE_&#8203;INTEL`]
  >> :CL_KERNEL_COMPILE_SUB_GROUP_SIZE_INTEL: pass:q[`CL_&#8203;KERNEL_&#8203;COMPILE_&#8203;SUB_&#8203;GROUP_&#8203;SIZE_&#8203;INTEL`]
     
     == Name Strings
     
- `extensions/cl_intel_required_subgroup_size.asciidoc`:
     
     [source]
     ----
  >> CL_KERNEL_COMPILE_SUB_GROUP_SIZE_INTEL          0x410A
     ----
     
     == New OpenCL C Optional Attribute Qualifiers
- `extensions/cl_intel_required_subgroup_size.asciidoc`:
     [width="100%",cols="<25%,<25%,<25%,<25%",options="header"]
     |====
     | *cl_kernel_sub_group_info* | Input Type | Return Type | Info. returned in _param_value_
  >> | {CL_KERNEL_COMPILE_SUB_GROUP_SIZE_INTEL}
     | `ignored`
     | `size_t`
     | Returns the sub-group size specified by the `+__attribute__((intel_reqd_sub_group_size(<int>)))+` qualifier.

## `CL_KERNEL_SPILL_MEM_SIZE_INTEL`  (container: `enums.4100`, value: 0x4109)
- `extensions/cl_intel_required_subgroup_size.asciidoc`:
     //:language: {basebackend@docbook:c++:cpp}
     
     :CL_DEVICE_SUB_GROUP_SIZES_INTEL: pass:q[`CL_&#8203;DEVICE_&#8203;SUB_&#8203;GROUP_&#8203;SIZES_&#8203;INTEL`]
  >> :CL_KERNEL_SPILL_MEM_SIZE_INTEL: pass:q[`CL_&#8203;KERNEL_&#8203;SPILL_&#8203;MEM_&#8203;SIZE_&#8203;INTEL`]
     :CL_KERNEL_COMPILE_SUB_GROUP_SIZE_INTEL: pass:q[`CL_&#8203;KERNEL_&#8203;COMPILE_&#8203;SUB_&#8203;GROUP_&#8203;SIZE_&#8203;INTEL`]
     
     == Name Strings
- `extensions/cl_intel_required_subgroup_size.asciidoc`:
     
     [source]
     ----
  >> CL_KERNEL_SPILL_MEM_SIZE_INTEL                  0x4109
     ----
     
     Accepted as the _param_name_ parameter of *clGetKernelSubGroupInfo* and/or
- `extensions/cl_intel_required_subgroup_size.asciidoc`:
     |====
     | *cl_kernel_work_group_info* | Return Type | Info. returned in _param_value_
     
  >> | {CL_KERNEL_SPILL_MEM_SIZE_INTEL}
     | `cl_ulong`
     | Returns the amount of spill memory used by a kernel.
     The meaning of this value will vary from implementation-to-implementation, however a return value of 0 will always indicate that compiler was able to 

## `CL_NV12_INTEL`  (container: `enums.4100`, value: 0x410E)
- `extensions/cl_intel_planar_yuv.asciidoc`:
     
     [source]
     ----
  >> #define CL_NV12_INTEL                               0x410E
     ----
     
     Accepted value for the _param_name_ parameter to *clGetDeviceInfo*:
- `extensions/cl_intel_planar_yuv.asciidoc`:
     | Image Type | Size of buffer that _host_ptr_ points to
     | `CL_MEM_OBJECT_IMAGE2D`
     | >= image_row_pitch * image_height + image_row_pitch * image_height / 2,
  >> for images with `image_channel_order` equal to `CL_NV12_INTEL`.
     |====
     --
     
- `extensions/cl_intel_planar_yuv.asciidoc`:
     | _image_channel_order_ of _mem_object_
     | Plane
     | _image_depth_ specified in _image_desc_
  >> | `CL_NV12_INTEL`
     | Y
     | 0
     | `CL_NV12_INTEL`
- `extensions/cl_intel_planar_yuv.asciidoc`:
     | `CL_NV12_INTEL`
     | Y
     | 0
  >> | `CL_NV12_INTEL`
     | UV
     | 1
     |====
- `extensions/cl_intel_planar_yuv.asciidoc`:
     |====
     | _image_channel_order_ of _mem_object_
     | _image_channel_data_type_ specified in _image_format_
  >> | `CL_NV12_INTEL`
     | `CL_UNORM_INT8`
     | `CL_NV12_INTEL`
     | `CL_UNSIGNED_INT8`
- `extensions/cl_intel_planar_yuv.asciidoc`:
     | _image_channel_data_type_ specified in _image_format_
     | `CL_NV12_INTEL`
     | `CL_UNORM_INT8`
  >> | `CL_NV12_INTEL`
     | `CL_UNSIGNED_INT8`
     |====
     

## `CL_MEM_ALLOC_BUFFER_LOCATION_INTEL`  (container: `enums.4190`, value: 0x419E)
- `extensions/cl_intel_mem_alloc_buffer_location.asciidoc`:
     
     [source,c]
     ----
  >> cl_mem_properties_intel props[] = {CL_MEM_ALLOC_BUFFER_LOCATION_INTEL, 2, 0};
     
     cl_mem test_mem = clCreateBufferWithPropertiesINTEL(
     context, props, flags,
- `extensions/cl_intel_mem_alloc_buffer_location.asciidoc`:
     [source,c]
     ----
     cl_mem_properties_intel property[3] = {
  >> CL_MEM_ALLOC_BUFFER_LOCATION_INTEL, 2,
     0};
     void *ptr = clDeviceMemAllocINTEL(context, device, property, size, alignment, &status);
     ----
- `extensions/cl_intel_mem_alloc_buffer_location.asciidoc`:
     [source,c]
     ----
     // Should return 2 given the previous allocation.
  >> clGetMemAllocInfoINTEL(context, ptr, CL_MEM_ALLOC_BUFFER_LOCATION_INTEL, sizeof(cl_uint), param_value, param_value_ret)
     ----
     
     
- `extensions/cl_intel_mem_alloc_buffer_location.asciidoc`:
     
     [source,c]
     ----
  >> #define CL_MEM_ALLOC_BUFFER_LOCATION_INTEL    0x419E
     ----
     
     Modifications to the OpenCL API Specification
- `extensions/cl_intel_mem_alloc_buffer_location.asciidoc`:
     | Property value
     | Description
     
  >> | +CL_MEM_ALLOC_BUFFER_LOCATION_INTEL+
     | +cl_uint+
     | Identifies the ID of global memory partition to which the memory should be allocated. The range of legal values is implementation-defined. If the va
     |====
- `extensions/cl_intel_mem_alloc_buffer_location.asciidoc`:
     [width="100%",cols="<34%,<33%,<33%",options="header"]
     |====
     | *cl_mem_info_intel* | Return type | Info. returned in _param_value_
  >> | `CL_MEM_ALLOC_BUFFER_LOCATION_INTEL`
     | cl_uint
     | Returns buffer location for the Unified Shared Memory allocation.
     

## `CL_SVM_INFO_ASSOCIATED_DEVICE_HANDLE_KHR`  (container: `enums.4190`, value: 0x419D)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SVM_INFO_BASE_PTR_KHR`  (container: `enums.4190`, value: 0x419B)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SVM_INFO_SIZE_KHR`  (container: `enums.4190`, value: 0x419C)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_CONTROLLED_TERMINATION_CAPABILITIES_ARM`  (container: `enums.41E0`, value: 0x41EE)
- `extensions/cl_arm_controlled_kernel_termination.asciidoc`:
     
     [source,c]
     ----
  >> CL_DEVICE_CONTROLLED_TERMINATION_CAPABILITIES_ARM   0x41EE
     
     #define CL_DEVICE_CONTROLLED_TERMINATION_SUCCESS_ARM (1 << 0)
     #define CL_DEVICE_CONTROLLED_TERMINATION_FAILURE_ARM (1 << 1)
- `extensions/cl_arm_controlled_kernel_termination.asciidoc`:
     | Return Type
     | Description
     
  >> | `CL_DEVICE_CONTROLLED_TERMINATION_CAPABILITIES_ARM`
     | `cl_device_controlled_termination_capabilities_arm`
     | Returns a bitfield describing which features of this extension
     are supported by the device. +

## `CL_DEVICE_JOB_SLOTS_ARM`  (container: `enums.41E0`, value: 0x41E0)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_MAX_WARP_COUNT_ARM`  (container: `enums.41E0`, value: 0x41EA)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     
     CL_DEVICE_SUPPORTED_REGISTER_ALLOCATIONS_ARM              0x41EB
     
  >> CL_DEVICE_MAX_WARP_COUNT_ARM                             0x41EA
     ----
     
     Accepted value for the _param_name_ parameter to *clSetKernelExecInfo*:
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     
     - {CL_DEVICE_SCHEDULING_WARP_THROTTLING_ARM} is set when the device supports
     {CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM}, {CL_KERNEL_MAX_WARP_COUNT_ARM}
  >> and {CL_DEVICE_MAX_WARP_COUNT_ARM}. +
     Missing before version 0.4.
     
     - {CL_DEVICE_SCHEDULING_COMPUTE_UNIT_BATCH_QUEUE_SIZE_ARM} is set when the
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     returned values can be passed to the `-fregister-allocation` build option. +
     Missing before version 0.3.
     
  >> | {CL_DEVICE_MAX_WARP_COUNT_ARM}
     | {cl_uint_TYPE}
     | Returns the maximum number of warps per compute unit a kernel may use. The
     value returned is an upper bound for any possible kernel. When

## `CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_ARM`  (container: `enums.41E0`, value: 0x41E4)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     
     [source,c]
     ----
  >> CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_ARM           0x41E4
     
     CL_DEVICE_SCHEDULING_KERNEL_BATCHING_ARM                (1 << 0)
     CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_ARM           (1 << 1)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     | Return Type
     | Description
     
  >> | `CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_ARM`
     | `cl_device_scheduling_controls_capabilities_arm`
     | Returns a bitfield of the scheduling controls this device supports:
     +
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     | {cl_uint_TYPE}
     | Returns the maximum number of warps per compute unit a kernel may use. The
     value returned is an upper bound for any possible kernel. When
  >> {CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_ARM} is not set, the call to
     {clGetDeviceInfo} returns {CL_INVALID_VALUE}. +
     Missing before version 0.4.
     |====

## `CL_DEVICE_SUPPORTED_REGISTER_ALLOCATIONS_ARM`  (container: `enums.41E0`, value: 0x41EB)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     CL_DEVICE_SCHEDULING_COMPUTE_UNIT_BATCH_QUEUE_SIZE_ARM  (1 << 6)
     CL_DEVICE_SCHEDULING_COMPUTE_UNIT_LIMIT_ARM             (1 << 7)
     
  >> CL_DEVICE_SUPPORTED_REGISTER_ALLOCATIONS_ARM              0x41EB
     
     CL_DEVICE_MAX_WARP_COUNT_ARM                             0x41EA
     ----
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     {CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM}. +
     Missing before version 0.6.
     
  >> | `CL_DEVICE_SUPPORTED_REGISTER_ALLOCATIONS_ARM`
     | `cl_int[]`
     | Returns an array of valid register allocations for this device. Each of the
     returned values can be passed to the `-fregister-allocation` build option. +

## `CL_EVENT_COMMAND_TERMINATION_REASON_ARM`  (container: `enums.41E0`, value: 0x41ED)
- `extensions/cl_arm_controlled_kernel_termination.asciidoc`:
     
     [source,c]
     ----
  >> CL_EVENT_COMMAND_TERMINATION_REASON_ARM       0x41ED
     ----
     
     Accepted value for the _param_name_ parameter to *clGetDeviceInfo*:
- `extensions/cl_arm_controlled_kernel_termination.asciidoc`:
     - `CL_DEVICE_CONTROLLED_TERMINATION_FAILURE_ARM` is set when calling the
     `arm_terminate_kernel` function with `ARM_TERMINATION_FAILURE` is supported. +
     - `CL_DEVICE_CONTROLLED_TERMINATION_QUERY_ARM` is set when
  >> `CL_EVENT_COMMAND_TERMINATION_REASON_ARM` and
     `CL_COMMAND_TERMINATED_ITSELF_WITH_FAILURE_ARM` are supported.
     
     |====
- `extensions/cl_arm_controlled_kernel_termination.asciidoc`:
     | Return Type
     | Description
     
  >> | `CL_EVENT_COMMAND_TERMINATION_REASON_ARM`
     | `cl_command_termination_reason_arm`
     | Returns the reason for a command's execution having ended: +
     - `CL_COMMAND_TERMINATION_COMPLETION_ARM` when the command ran to completion +

## `CL_IMPORT_ANDROID_HARDWARE_BUFFER_LAYER_INDEX_ARM`  (container: `enums.41E0`, value: 0x41F0)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMPORT_ANDROID_HARDWARE_BUFFER_PLANE_INDEX_ARM`  (container: `enums.41E0`, value: 0x41EF)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMPORT_DMA_BUF_DATA_CONSISTENCY_WITH_HOST_ARM`  (container: `enums.41E0`, value: 0x41E3)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_IMPORT_TYPE_ANDROID_HARDWARE_BUFFER_ARM`  (container: `enums.41E0`, value: 0x41E2)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_KERNEL_EXEC_INFO_COMPUTE_UNIT_MAX_QUEUED_BATCHES_ARM`  (container: `enums.41E0`, value: 0x41F1)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM            0x41E5
     CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM   0x41E6
     CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM                0x41E8
  >> CL_KERNEL_EXEC_INFO_COMPUTE_UNIT_MAX_QUEUED_BATCHES_ARM 0x41F1
     ----
     
     Accepted value for the _properties_ parameter to *clCreateCommandQueueWithProperties*:
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     Missing before version 0.4.
     
     - {CL_DEVICE_SCHEDULING_COMPUTE_UNIT_BATCH_QUEUE_SIZE_ARM} is set when the
  >> device supports {CL_KERNEL_EXEC_INFO_COMPUTE_UNIT_MAX_QUEUED_BATCHES_ARM}. +
     Missing before version 0.5.
     
     - {CL_DEVICE_SCHEDULING_COMPUTE_UNIT_LIMIT_ARM} is set when the device supports
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     will fail and return {CL_INVALID_VALUE}. +
     Missing before version 0.4.
     
  >> | {CL_KERNEL_EXEC_INFO_COMPUTE_UNIT_MAX_QUEUED_BATCHES_ARM}
     | {cl_uint_TYPE}
     | Limit the number of workgroup batches each compute unit can have in its queue. +
     Acceptable values depend on the device. If a value not supported by the device

## `CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM`  (container: `enums.41E0`, value: 0x41E8)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     ----
     CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM            0x41E5
     CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM   0x41E6
  >> CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM                0x41E8
     CL_KERNEL_EXEC_INFO_COMPUTE_UNIT_MAX_QUEUED_BATCHES_ARM 0x41F1
     ----
     
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     supports the `-fregister-allocation` option.
     
     - {CL_DEVICE_SCHEDULING_WARP_THROTTLING_ARM} is set when the device supports
  >> {CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM}, {CL_KERNEL_MAX_WARP_COUNT_ARM}
     and {CL_DEVICE_MAX_WARP_COUNT_ARM}. +
     Missing before version 0.4.
     
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     is not possible due to hardware constraints, the greatest possible modification
     will be used.
     
  >> | {CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM}
     | {cl_uint_TYPE}
     | Limit the number of warps allowed to run in each compute unit for this kernel. +
     The value passed must be greater than 0 and smaller than or equal to

## `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`  (container: `enums.41E0`, value: 0x41E5)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     
     [source,c]
     ----
  >> CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM            0x41E5
     CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM   0x41E6
     CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM                0x41E8
     CL_KERNEL_EXEC_INFO_COMPUTE_UNIT_MAX_QUEUED_BATCHES_ARM 0x41F1
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     `CL_QUEUE_KERNEL_BATCHING_ARM`.
     +
     - `CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_ARM` is set when the device
  >> supports `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`.
     +
     - `CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_MODIFIER_ARM` is set when the
     device supports `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM`.
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     | Type
     | Description
     
  >> | `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`
     | `cl_uint`
     | Set the size of batches of work groups distributed to compute units.
     The value is a number of work groups. If set to 0, then the runtime
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     | `cl_int`
     | Modify the size of batches of work groups distributed to compute units.
     
  >> On devices that support `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`, the value is
     a number of work groups added to the batch size calculated by the runtime (when
     `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM` set to 0) or set by the application
     (when `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM` set to a value greater than 0).
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     
     On devices that support `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`, the value is
     a number of work groups added to the batch size calculated by the runtime (when
  >> `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM` set to 0) or set by the application
     (when `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM` set to a value greater than 0).
     
     On devices that do not support `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`, the
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     On devices that support `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`, the value is
     a number of work groups added to the batch size calculated by the runtime (when
     `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM` set to 0) or set by the application
  >> (when `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM` set to a value greater than 0).
     
     On devices that do not support `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`, the
     value is a number in the range [-31,+31]. When set to 0, the runtime-selected

## `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM`  (container: `enums.41E0`, value: 0x41E6)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     [source,c]
     ----
     CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM            0x41E5
  >> CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM   0x41E6
     CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM                0x41E8
     CL_KERNEL_EXEC_INFO_COMPUTE_UNIT_MAX_QUEUED_BATCHES_ARM 0x41F1
     ----
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     supports `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`.
     +
     - `CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_MODIFIER_ARM` is set when the
  >> device supports `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM`.
     - `CL_DEVICE_SCHEDULING_DEFERRED_FLUSH_ARM` is set when the device supports
     `CL_QUEUE_DEFERRED_FLUSH_ARM`.
     
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     ND-range. When a value is not directly usable due to device-specific
     constraints, it will be rounded up to the next usable value.
     
  >> | `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM`
     | `cl_int`
     | Modify the size of batches of work groups distributed to compute units.
     
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     Some features in this extension interact with `cl_arm_thread_limit_hint`.
     
     If `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM` or
  >> `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM` is set to a non-default
     value at the time a kernel is enqueued, then any thread limit hint specified
     in the kernel source using the `arm_thread_limit_hint` attribute will be
     ignored.

## `CL_KERNEL_MAX_WARP_COUNT_ARM`  (container: `enums.41E0`, value: 0x41E9)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     
     [source,c]
     ----
  >> CL_KERNEL_MAX_WARP_COUNT_ARM 0x41E9
     ----
     
     == New build options
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     supports the `-fregister-allocation` option.
     
     - {CL_DEVICE_SCHEDULING_WARP_THROTTLING_ARM} is set when the device supports
  >> {CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM}, {CL_KERNEL_MAX_WARP_COUNT_ARM}
     and {CL_DEVICE_MAX_WARP_COUNT_ARM}. +
     Missing before version 0.4.
     
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     | {cl_uint_TYPE}
     | Limit the number of warps allowed to run in each compute unit for this kernel. +
     The value passed must be greater than 0 and smaller than or equal to
  >> {CL_KERNEL_MAX_WARP_COUNT_ARM}, otherwise the call to {clSetKernelExecInfo}
     will fail and return {CL_INVALID_VALUE}. +
     Missing before version 0.4.
     
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     | Return type
     | Description
     
  >> | {CL_KERNEL_MAX_WARP_COUNT_ARM}
     | {cl_uint_TYPE}
     | Returns the maximum number of warps this kernel can use per compute unit. +
     Missing before version 0.4.

## `CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM`  (container: `enums.41E0`, value: 0x41F3)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     ----
     CL_QUEUE_KERNEL_BATCHING_ARM    0x41E7
     CL_QUEUE_DEFERRED_FLUSH_ARM     0x41EC
  >> CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM 0x41F3
     ----
     
     Accepted value for the _param_name_ parameter to *clGetKernelInfo*:
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     Missing before version 0.5.
     
     - {CL_DEVICE_SCHEDULING_COMPUTE_UNIT_LIMIT_ARM} is set when the device supports
  >> {CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM}. +
     Missing before version 0.6.
     
     | `CL_DEVICE_SUPPORTED_REGISTER_ALLOCATIONS_ARM`
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     `CL_TRUE` means flush operations are deferred. Defaults to `CL_TRUE`. +
     Missing before version 0.2.
     
  >> | {CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM}
     | {cl_uint_TYPE}
     | Set a limit for the number of compute units this queue is allowed to use.
     The limit provided must be greater than 0 and less than or equal to

## `CL_QUEUE_DEFERRED_FLUSH_ARM`  (container: `enums.41E0`, value: 0x41EC)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     [source,c]
     ----
     CL_QUEUE_KERNEL_BATCHING_ARM    0x41E7
  >> CL_QUEUE_DEFERRED_FLUSH_ARM     0x41EC
     CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM 0x41F3
     ----
     
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     - `CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_MODIFIER_ARM` is set when the
     device supports `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM`.
     - `CL_DEVICE_SCHEDULING_DEFERRED_FLUSH_ARM` is set when the device supports
  >> `CL_QUEUE_DEFERRED_FLUSH_ARM`.
     
     - `CL_DEVICE_SCHEDULING_REGISTER_ALLOCATION_ARM` is set when the device compiler
     supports the `-fregister-allocation` option.
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     device. `CL_TRUE` means kernels will be batched, `CL_FALSE` that they will not.
     Defaults to `CL_TRUE`.
     
  >> | `CL_QUEUE_DEFERRED_FLUSH_ARM`
     | `cl_bool`
     | Whether flush operations are performed in the thread triggering the flush or
     deferred for execution in another thread managed by the OpenCL runtime.

## `CL_QUEUE_JOB_SLOT_ARM`  (container: `enums.41E0`, value: 0x41E1)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_QUEUE_KERNEL_BATCHING_ARM`  (container: `enums.41E0`, value: 0x41E7)
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     
     [source,c]
     ----
  >> CL_QUEUE_KERNEL_BATCHING_ARM    0x41E7
     CL_QUEUE_DEFERRED_FLUSH_ARM     0x41EC
     CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM 0x41F3
     ----
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     | Returns a bitfield of the scheduling controls this device supports:
     +
     - `CL_DEVICE_SCHEDULING_KERNEL_BATCHING_ARM` is set when the device supports
  >> `CL_QUEUE_KERNEL_BATCHING_ARM`.
     +
     - `CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_ARM` is set when the device
     supports `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM`.
- `extensions/cl_arm_scheduling_controls.asciidoc`:
     | Type
     | Description
     
  >> | `CL_QUEUE_KERNEL_BATCHING_ARM`
     | `cl_bool`
     | Whether kernels enqueued to this queue should be batched for submission to the
     device. `CL_TRUE` means kernels will be batched, `CL_FALSE` that they will not.

## `CL_COMMAND_READ_HOST_PIPE_INTEL`  (container: `enums.4210`, value: 0x4214)
- `extensions/cl_intel_program_scope_host_pipe.asciidoc`:
     
     [source, c]
     ----
  >> #define CL_COMMAND_READ_HOST_PIPE_INTEL   0x4214
     #define CL_COMMAND_WRITE_HOST_PIPE_INTEL  0x4215
     #define CL_PROGRAM_NUM_HOST_PIPES_INTEL   0x4216
     #define CL_PROGRAM_HOST_PIPE_NAMES_INTEL  0x4217
- `extensions/cl_intel_program_scope_host_pipe.asciidoc`:
     |===
     | Events Created By |Event Command Type
     | clEnqueueReadHostPipeINTEL
  >> | CL_COMMAND_READ_HOST_PIPE_INTEL
     | clEnqueueWriteHostPipeINTEL
     | CL_COMMAND_WRITE_HOST_PIPE_INTEL
     |===

## `CL_COMMAND_WRITE_HOST_PIPE_INTEL`  (container: `enums.4210`, value: 0x4215)
- `extensions/cl_intel_program_scope_host_pipe.asciidoc`:
     [source, c]
     ----
     #define CL_COMMAND_READ_HOST_PIPE_INTEL   0x4214
  >> #define CL_COMMAND_WRITE_HOST_PIPE_INTEL  0x4215
     #define CL_PROGRAM_NUM_HOST_PIPES_INTEL   0x4216
     #define CL_PROGRAM_HOST_PIPE_NAMES_INTEL  0x4217
     ----
- `extensions/cl_intel_program_scope_host_pipe.asciidoc`:
     | clEnqueueReadHostPipeINTEL
     | CL_COMMAND_READ_HOST_PIPE_INTEL
     | clEnqueueWriteHostPipeINTEL
  >> | CL_COMMAND_WRITE_HOST_PIPE_INTEL
     |===
     
     == Issues

## `CL_DEVICE_MAX_HOST_READ_PIPES_INTEL`  (container: `enums.4210`, value: 0x4211)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_MAX_HOST_WRITE_PIPES_INTEL`  (container: `enums.4210`, value: 0x4212)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_KERNEL_ARG_HOST_ACCESSIBLE_PIPE_INTEL`  (container: `enums.4210`, value: 0x4210)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_CHANNEL_INTEL`  (container: `enums.4210`, value: 0x4213)
- `extensions/cl_intel_mem_channel_property.asciidoc`:
     
     [source,c]
     ----
  >> #define CL_MEM_CHANNEL_INTEL        0x4213
     ----
     
     Modifications to the OpenCL API Specification
- `extensions/cl_intel_mem_channel_property.asciidoc`:
     | Property value
     | Description
     
  >> | +CL_MEM_CHANNEL_INTEL+
     | +cl_uint+
     | Identifies the channel/region to which the buffer should be mapped.  The range of legal values is implementation-defined.  This parameter acts as a 
     |====

## `CL_MEM_DEVICE_ID_INTEL`  (container: `enums.4210`, value: 0x4219)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_MEM_LOCALLY_UNCACHED_RESOURCE_INTEL`  (container: `enums.4210`, value: 0x4218)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_PROGRAM_HOST_PIPE_NAMES_INTEL`  (container: `enums.4210`, value: 0x4217)
- `extensions/cl_intel_program_scope_host_pipe.asciidoc`:
     #define CL_COMMAND_READ_HOST_PIPE_INTEL   0x4214
     #define CL_COMMAND_WRITE_HOST_PIPE_INTEL  0x4215
     #define CL_PROGRAM_NUM_HOST_PIPES_INTEL   0x4216
  >> #define CL_PROGRAM_HOST_PIPE_NAMES_INTEL  0x4217
     ----
     
     
- `extensions/cl_intel_program_scope_host_pipe.asciidoc`:
     | CL_PROGRAM_NUM_HOST_PIPES_INTEL
     | size_t
     | Returns the number of host pipes declared in program. This information is only available after a successful program executable has been built for at
  >> | CL_PROGRAM_HOST_PIPE_NAMES_INTEL
     | char[]
     | Returns a semi-colon separated list of host pipe names in program. This information is only available after a successful program executable has been
     |===

## `CL_PROGRAM_NUM_HOST_PIPES_INTEL`  (container: `enums.4210`, value: 0x4216)
- `extensions/cl_intel_program_scope_host_pipe.asciidoc`:
     ----
     #define CL_COMMAND_READ_HOST_PIPE_INTEL   0x4214
     #define CL_COMMAND_WRITE_HOST_PIPE_INTEL  0x4215
  >> #define CL_PROGRAM_NUM_HOST_PIPES_INTEL   0x4216
     #define CL_PROGRAM_HOST_PIPE_NAMES_INTEL  0x4217
     ----
     
- `extensions/cl_intel_program_scope_host_pipe.asciidoc`:
     
     [width="100%",cols="25,25,25"]
     |===
  >> | CL_PROGRAM_NUM_HOST_PIPES_INTEL
     | size_t
     | Returns the number of host pipes declared in program. This information is only available after a successful program executable has been built for at
     | CL_PROGRAM_HOST_PIPE_NAMES_INTEL

## `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_IMG`  (container: `enums.4220`, value: 0x4224)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_ROUND_ROBIN_IMG`  (container: `enums.4220`, value: 0x422A)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_TASK_DEMAND_IMG`  (container: `enums.4220`, value: 0x4229)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_EXECUTE_COUNT_IMG`  (container: `enums.4220`, value: 0x422B)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_IMG`  (container: `enums.4220`, value: 0x4223)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_LINEAR_ORDER_IMG`  (container: `enums.4220`, value: 0x4225)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_MORTON_ORDER_IMG`  (container: `enums.4220`, value: 0x4226)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_THREED_MORTON_ORDER_IMG`  (container: `enums.4220`, value: 0x4228)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_TWOD_MORTON_ORDER_IMG`  (container: `enums.4220`, value: 0x4227)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_IMG`  (container: `enums.4220`, value: 0x4222)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SEMAPHORE_FAST_PATH_IMG`  (container: `enums.4220`, value: 0x422D)
- NO SPEC MENTIONS in api/, env/, extensions/

## `CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG`  (container: `enums.4220`, value: 0x4221)
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     [source,opencl]
     ----
     CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG 0x4220
  >> CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG                 0x4221
     ----
     
     == Modifications to the OpenCL API Specification
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     
     In Section 5.6, add the following text as a new row in the SVM Allocation Properties table:
     
  >> CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG
     
     Provides an external dma_buf handle to import into the new SVM allocation.
     
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     
     Add the following text to the list of error values returned by clSVMAllocWithProperties
     
  >> CL_INVALID_PROPERTY if CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG is specificed as part of properties,
     and properties does not include a valid CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG.
     
     CL_INVALID_PROPERTY if CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG is specificed as part of properties,
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     and properties does not include a valid CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG.
     
     CL_INVALID_PROPERTY if CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG is specificed as part of properties,
  >> and properties does not include a valid CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG.
     
     == Example Usage ==
     
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     [source,opencl]
     ----
     const cl_svm_alloc_properties_khr* properties = {
  >> (cl_svm_alloc_properties_khr) CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG,
     (cl_svm_alloc_properties_khr) external_fd,
     (cl_svm_alloc_properties_khr) CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG,
     (cl_svm_alloc_properties_khr) svm_virtual_address,

## `CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG`  (container: `enums.4220`, value: 0x4220)
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     
     [source,opencl]
     ----
  >> CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG 0x4220
     CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG                 0x4221
     ----
     
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     
     Provides an external dma_buf handle to import into the new SVM allocation.
     
  >> CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG
     
     Provides the virtual address that the new SVM allocation must map to.
     +
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     Add the following text to the list of error values returned by clSVMAllocWithProperties
     
     CL_INVALID_PROPERTY if CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG is specificed as part of properties,
  >> and properties does not include a valid CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG.
     
     CL_INVALID_PROPERTY if CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG is specificed as part of properties,
     and properties does not include a valid CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG.
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     CL_INVALID_PROPERTY if CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG is specificed as part of properties,
     and properties does not include a valid CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG.
     
  >> CL_INVALID_PROPERTY if CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG is specificed as part of properties,
     and properties does not include a valid CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG.
     
     == Example Usage ==
- `extensions/cl_img_unified_svm_external_memory_dma_buf.asciidoc`:
     const cl_svm_alloc_properties_khr* properties = {
     (cl_svm_alloc_properties_khr) CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG,
     (cl_svm_alloc_properties_khr) external_fd,
  >> (cl_svm_alloc_properties_khr) CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG,
     (cl_svm_alloc_properties_khr) svm_virtual_address,
     0
     };

## `CL_KERNEL_EXEC_INFO_DEVICE_PTRS_EXT`  (container: `enums.5000`, value: 0x5002)
- `api/opencl_runtime_layer.asciidoc`:
     {CL_TRUE}.
     
     ifdef::cl_ext_buffer_device_address[]
  >> | {CL_KERNEL_EXEC_INFO_DEVICE_PTRS_EXT_anchor}
     
     [version-note]
     | {cl_mem_device_address_ext_TYPE}[]
- `api/opencl_runtime_layer.asciidoc`:
     ifdef::cl_ext_buffer_device_address[]
     | {CL_KERNEL_EXEC_INFO_DEVICE_PTRS_EXT_anchor}
     
  >> [version-note]
     | {cl_mem_device_address_ext_TYPE}[]
     | Device pointers must reference locations contained entirely within
     buffers that are passed to kernel as arguments, or that are passed
- `api/opencl_runtime_layer.asciidoc`:
     system SVM allocations.
     ifdef::cl_ext_buffer_device_address[]
     * {CL_INVALID_OPERATION} if _param_name_ is
  >> {CL_KERNEL_EXEC_INFO_DEVICE_PTRS_EXT} and no devices in the context
     associated with _kernel_ support the {cl_ext_buffer_device_address_EXT}
     extension.
     endif::cl_ext_buffer_device_address[]

## `CL_MEM_DEVICE_PRIVATE_ADDRESS_EXT`  (container: `enums.5000`, value: 0x5000)
- `api/opencl_runtime_layer.asciidoc`:
     
     ifdef::cl_ext_buffer_device_address[]
     
  >> | {CL_MEM_DEVICE_PRIVATE_ADDRESS_EXT_anchor}
     
     [version-note]
     | {cl_bool_TYPE}
- `api/opencl_runtime_layer.asciidoc`:
     
     | {CL_MEM_DEVICE_PRIVATE_ADDRESS_EXT_anchor}
     
  >> [version-note]
     | {cl_bool_TYPE}
     | When set to {CL_TRUE}, specifies that the buffer must have a single fixed
     device-side address for its lifetime, and the address can be queried via {clGetMemObjectInfo}.
- `api/opencl_runtime_layer.asciidoc`:
     a device's memory, but might not be necessarily so, as long as the address
     range of the buffer remains constant.
     
  >> The device addresses of sub-buffers derived from {CL_MEM_DEVICE_PRIVATE_ADDRESS_EXT}
     allocated buffers can be computed by adding the sub-buffer origin to the
     device-specific start address.
     
- `api/opencl_runtime_layer.asciidoc`:
     the AHardwareBuffer format is not `AHARDWAREBUFFER_FORMAT_BLOB`
     endif::cl_khr_external_memory_android_hardware_buffer[]
     ifdef::cl_ext_buffer_device_address[]
  >> ** if _properties_ includes {CL_MEM_DEVICE_PRIVATE_ADDRESS_EXT} and there
     are no devices in the context that support the
     {cl_ext_buffer_device_address_EXT} extension
     endif::cl_ext_buffer_device_address[]
- `api/opencl_runtime_layer.asciidoc`:
     [version-note]
     |  {cl_mem_device_address_ext_TYPE}[]
     | If _memobj_ was created using {clCreateBufferWithProperties} with
  >> the {CL_MEM_DEVICE_PRIVATE_ADDRESS_EXT} property set to {CL_TRUE},
     returns a list of device addresses for the buffer, one for each
     device in the context in the same order as the list of devices
     passed to {clCreateContext}.
- `api/opencl_runtime_layer.asciidoc`:
     * {CL_INVALID_OPERATION}
     ** if the {cl_ext_buffer_device_address_EXT} extension is supported, if
     _param_name_ is {CL_MEM_DEVICE_ADDRESS_EXT}, and if _memobj_ was not created
  >> with the {CL_MEM_DEVICE_PRIVATE_ADDRESS_EXT} property set to {CL_TRUE}
     endif::cl_ext_buffer_device_address[]
     ifdef::cl_khr_dx9_media_sharing[]
     * {CL_INVALID_DX9_MEDIA_SURFACE_KHR}
