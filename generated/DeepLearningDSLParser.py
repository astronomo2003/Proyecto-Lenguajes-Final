# Generated from grammar/DeepLearningDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,408,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,82,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,96,
        8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,3,5,114,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,132,8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,
        142,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,
        10,155,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,164,8,11,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,3,13,173,8,13,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,3,15,183,8,15,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,18,1,18,1,18,1,18,1,18,3,18,197,8,18,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,3,19,230,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,1,21,3,21,247,8,21,1,22,1,22,1,22,1,22,
        1,22,3,22,254,8,22,1,23,1,23,1,24,1,24,3,24,260,8,24,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,28,1,28,1,28,3,28,295,8,28,1,29,1,29,1,29,1,29,3,29,301,
        8,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        3,31,315,8,31,1,32,1,32,1,32,1,32,3,32,321,8,32,1,33,1,33,1,33,1,
        33,1,33,3,33,328,8,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,3,34,369,8,34,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,387,8,
        35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,3,36,406,8,36,1,36,0,0,37,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,0,2,1,0,23,26,1,0,34,39,415,0,74,1,0,0,0,
        2,81,1,0,0,0,4,95,1,0,0,0,6,97,1,0,0,0,8,101,1,0,0,0,10,113,1,0,
        0,0,12,115,1,0,0,0,14,131,1,0,0,0,16,133,1,0,0,0,18,141,1,0,0,0,
        20,154,1,0,0,0,22,163,1,0,0,0,24,165,1,0,0,0,26,172,1,0,0,0,28,174,
        1,0,0,0,30,182,1,0,0,0,32,184,1,0,0,0,34,188,1,0,0,0,36,196,1,0,
        0,0,38,229,1,0,0,0,40,231,1,0,0,0,42,246,1,0,0,0,44,253,1,0,0,0,
        46,255,1,0,0,0,48,259,1,0,0,0,50,261,1,0,0,0,52,273,1,0,0,0,54,281,
        1,0,0,0,56,294,1,0,0,0,58,300,1,0,0,0,60,302,1,0,0,0,62,314,1,0,
        0,0,64,320,1,0,0,0,66,327,1,0,0,0,68,368,1,0,0,0,70,386,1,0,0,0,
        72,405,1,0,0,0,74,75,3,2,1,0,75,76,5,0,0,1,76,1,1,0,0,0,77,78,3,
        4,2,0,78,79,3,2,1,0,79,82,1,0,0,0,80,82,1,0,0,0,81,77,1,0,0,0,81,
        80,1,0,0,0,82,3,1,0,0,0,83,84,3,6,3,0,84,85,5,47,0,0,85,96,1,0,0,
        0,86,96,3,40,20,0,87,96,3,48,24,0,88,96,3,54,27,0,89,90,3,62,31,
        0,90,91,5,47,0,0,91,96,1,0,0,0,92,93,3,8,4,0,93,94,5,47,0,0,94,96,
        1,0,0,0,95,83,1,0,0,0,95,86,1,0,0,0,95,87,1,0,0,0,95,88,1,0,0,0,
        95,89,1,0,0,0,95,92,1,0,0,0,96,5,1,0,0,0,97,98,5,51,0,0,98,99,5,
        27,0,0,99,100,3,8,4,0,100,7,1,0,0,0,101,102,3,12,6,0,102,103,3,10,
        5,0,103,9,1,0,0,0,104,105,5,28,0,0,105,106,3,12,6,0,106,107,3,10,
        5,0,107,114,1,0,0,0,108,109,5,29,0,0,109,110,3,12,6,0,110,111,3,
        10,5,0,111,114,1,0,0,0,112,114,1,0,0,0,113,104,1,0,0,0,113,108,1,
        0,0,0,113,112,1,0,0,0,114,11,1,0,0,0,115,116,3,16,8,0,116,117,3,
        14,7,0,117,13,1,0,0,0,118,119,5,30,0,0,119,120,3,16,8,0,120,121,
        3,14,7,0,121,132,1,0,0,0,122,123,5,31,0,0,123,124,3,16,8,0,124,125,
        3,14,7,0,125,132,1,0,0,0,126,127,5,32,0,0,127,128,3,16,8,0,128,129,
        3,14,7,0,129,132,1,0,0,0,130,132,1,0,0,0,131,118,1,0,0,0,131,122,
        1,0,0,0,131,126,1,0,0,0,131,130,1,0,0,0,132,15,1,0,0,0,133,134,3,
        20,10,0,134,135,3,18,9,0,135,17,1,0,0,0,136,137,5,33,0,0,137,138,
        3,20,10,0,138,139,3,18,9,0,139,142,1,0,0,0,140,142,1,0,0,0,141,136,
        1,0,0,0,141,140,1,0,0,0,142,19,1,0,0,0,143,155,5,51,0,0,144,155,
        5,48,0,0,145,155,5,49,0,0,146,155,5,50,0,0,147,148,5,40,0,0,148,
        149,3,8,4,0,149,150,5,41,0,0,150,155,1,0,0,0,151,155,3,26,13,0,152,
        155,3,62,31,0,153,155,3,22,11,0,154,143,1,0,0,0,154,144,1,0,0,0,
        154,145,1,0,0,0,154,146,1,0,0,0,154,147,1,0,0,0,154,151,1,0,0,0,
        154,152,1,0,0,0,154,153,1,0,0,0,155,21,1,0,0,0,156,157,5,29,0,0,
        157,164,3,20,10,0,158,159,3,24,12,0,159,160,5,40,0,0,160,161,3,8,
        4,0,161,162,5,41,0,0,162,164,1,0,0,0,163,156,1,0,0,0,163,158,1,0,
        0,0,164,23,1,0,0,0,165,166,7,0,0,0,166,25,1,0,0,0,167,168,5,44,0,
        0,168,169,3,28,14,0,169,170,5,45,0,0,170,173,1,0,0,0,171,173,3,38,
        19,0,172,167,1,0,0,0,172,171,1,0,0,0,173,27,1,0,0,0,174,175,3,32,
        16,0,175,176,3,30,15,0,176,29,1,0,0,0,177,178,5,46,0,0,178,179,3,
        32,16,0,179,180,3,30,15,0,180,183,1,0,0,0,181,183,1,0,0,0,182,177,
        1,0,0,0,182,181,1,0,0,0,183,31,1,0,0,0,184,185,5,44,0,0,185,186,
        3,34,17,0,186,187,5,45,0,0,187,33,1,0,0,0,188,189,3,8,4,0,189,190,
        3,36,18,0,190,35,1,0,0,0,191,192,5,46,0,0,192,193,3,8,4,0,193,194,
        3,36,18,0,194,197,1,0,0,0,195,197,1,0,0,0,196,191,1,0,0,0,196,195,
        1,0,0,0,197,37,1,0,0,0,198,199,5,12,0,0,199,200,5,40,0,0,200,201,
        3,8,4,0,201,202,5,41,0,0,202,230,1,0,0,0,203,204,5,13,0,0,204,205,
        5,40,0,0,205,206,3,8,4,0,206,207,5,41,0,0,207,230,1,0,0,0,208,209,
        5,14,0,0,209,210,5,40,0,0,210,211,3,8,4,0,211,212,5,46,0,0,212,213,
        3,8,4,0,213,214,5,41,0,0,214,230,1,0,0,0,215,216,5,15,0,0,216,217,
        5,40,0,0,217,218,3,8,4,0,218,219,5,46,0,0,219,220,3,8,4,0,220,221,
        5,41,0,0,221,230,1,0,0,0,222,223,5,16,0,0,223,224,5,40,0,0,224,225,
        3,8,4,0,225,226,5,46,0,0,226,227,3,8,4,0,227,228,5,41,0,0,228,230,
        1,0,0,0,229,198,1,0,0,0,229,203,1,0,0,0,229,208,1,0,0,0,229,215,
        1,0,0,0,229,222,1,0,0,0,230,39,1,0,0,0,231,232,5,1,0,0,232,233,5,
        40,0,0,233,234,3,44,22,0,234,235,5,41,0,0,235,236,5,42,0,0,236,237,
        3,2,1,0,237,238,5,43,0,0,238,239,3,42,21,0,239,41,1,0,0,0,240,241,
        5,2,0,0,241,242,5,42,0,0,242,243,3,2,1,0,243,244,5,43,0,0,244,247,
        1,0,0,0,245,247,1,0,0,0,246,240,1,0,0,0,246,245,1,0,0,0,247,43,1,
        0,0,0,248,249,3,8,4,0,249,250,3,46,23,0,250,251,3,8,4,0,251,254,
        1,0,0,0,252,254,3,8,4,0,253,248,1,0,0,0,253,252,1,0,0,0,254,45,1,
        0,0,0,255,256,7,1,0,0,256,47,1,0,0,0,257,260,3,50,25,0,258,260,3,
        52,26,0,259,257,1,0,0,0,259,258,1,0,0,0,260,49,1,0,0,0,261,262,5,
        3,0,0,262,263,5,40,0,0,263,264,3,6,3,0,264,265,5,47,0,0,265,266,
        3,44,22,0,266,267,5,47,0,0,267,268,3,6,3,0,268,269,5,41,0,0,269,
        270,5,42,0,0,270,271,3,2,1,0,271,272,5,43,0,0,272,51,1,0,0,0,273,
        274,5,4,0,0,274,275,5,40,0,0,275,276,3,44,22,0,276,277,5,41,0,0,
        277,278,5,42,0,0,278,279,3,2,1,0,279,280,5,43,0,0,280,53,1,0,0,0,
        281,282,5,5,0,0,282,283,5,51,0,0,283,284,5,40,0,0,284,285,3,56,28,
        0,285,286,5,41,0,0,286,287,5,42,0,0,287,288,3,2,1,0,288,289,3,60,
        30,0,289,290,5,43,0,0,290,55,1,0,0,0,291,292,5,51,0,0,292,295,3,
        58,29,0,293,295,1,0,0,0,294,291,1,0,0,0,294,293,1,0,0,0,295,57,1,
        0,0,0,296,297,5,46,0,0,297,298,5,51,0,0,298,301,3,58,29,0,299,301,
        1,0,0,0,300,296,1,0,0,0,300,299,1,0,0,0,301,59,1,0,0,0,302,303,5,
        6,0,0,303,304,3,8,4,0,304,305,5,47,0,0,305,61,1,0,0,0,306,307,5,
        51,0,0,307,308,5,40,0,0,308,309,3,64,32,0,309,310,5,41,0,0,310,315,
        1,0,0,0,311,315,3,68,34,0,312,315,3,70,35,0,313,315,3,72,36,0,314,
        306,1,0,0,0,314,311,1,0,0,0,314,312,1,0,0,0,314,313,1,0,0,0,315,
        63,1,0,0,0,316,317,3,8,4,0,317,318,3,66,33,0,318,321,1,0,0,0,319,
        321,1,0,0,0,320,316,1,0,0,0,320,319,1,0,0,0,321,65,1,0,0,0,322,323,
        5,46,0,0,323,324,3,8,4,0,324,325,3,66,33,0,325,328,1,0,0,0,326,328,
        1,0,0,0,327,322,1,0,0,0,327,326,1,0,0,0,328,67,1,0,0,0,329,330,5,
        7,0,0,330,331,5,40,0,0,331,332,3,8,4,0,332,333,5,46,0,0,333,334,
        3,8,4,0,334,335,5,41,0,0,335,369,1,0,0,0,336,337,5,8,0,0,337,338,
        5,40,0,0,338,339,3,8,4,0,339,340,5,46,0,0,340,341,3,8,4,0,341,342,
        5,46,0,0,342,343,3,8,4,0,343,344,5,41,0,0,344,369,1,0,0,0,345,346,
        5,9,0,0,346,347,5,40,0,0,347,348,3,8,4,0,348,349,5,46,0,0,349,350,
        3,8,4,0,350,351,5,46,0,0,351,352,3,8,4,0,352,353,5,41,0,0,353,369,
        1,0,0,0,354,355,5,10,0,0,355,356,5,40,0,0,356,357,3,8,4,0,357,358,
        5,46,0,0,358,359,3,8,4,0,359,360,5,41,0,0,360,369,1,0,0,0,361,362,
        5,11,0,0,362,363,5,40,0,0,363,364,3,8,4,0,364,365,5,46,0,0,365,366,
        3,8,4,0,366,367,5,41,0,0,367,369,1,0,0,0,368,329,1,0,0,0,368,336,
        1,0,0,0,368,345,1,0,0,0,368,354,1,0,0,0,368,361,1,0,0,0,369,69,1,
        0,0,0,370,371,5,17,0,0,371,372,5,40,0,0,372,373,5,50,0,0,373,387,
        5,41,0,0,374,375,5,18,0,0,375,376,5,40,0,0,376,377,5,50,0,0,377,
        378,5,46,0,0,378,379,3,8,4,0,379,380,5,41,0,0,380,387,1,0,0,0,381,
        382,5,19,0,0,382,383,5,40,0,0,383,384,3,8,4,0,384,385,5,41,0,0,385,
        387,1,0,0,0,386,370,1,0,0,0,386,374,1,0,0,0,386,381,1,0,0,0,387,
        71,1,0,0,0,388,389,5,20,0,0,389,390,5,40,0,0,390,391,3,8,4,0,391,
        392,5,41,0,0,392,406,1,0,0,0,393,394,5,21,0,0,394,395,5,40,0,0,395,
        396,3,8,4,0,396,397,5,46,0,0,397,398,3,8,4,0,398,399,5,41,0,0,399,
        406,1,0,0,0,400,401,5,22,0,0,401,402,5,40,0,0,402,403,3,8,4,0,403,
        404,5,41,0,0,404,406,1,0,0,0,405,388,1,0,0,0,405,393,1,0,0,0,405,
        400,1,0,0,0,406,73,1,0,0,0,22,81,95,113,131,141,154,163,172,182,
        196,229,246,253,259,294,300,314,320,327,368,386,405
    ]

class DeepLearningDSLParser ( Parser ):

    grammarFileName = "DeepLearningDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'while'", 
                     "'def'", "'return'", "'linear_regression'", "'mlp_classifier'", 
                     "'neural_network'", "'predict'", "'train'", "'transpose'", 
                     "'inverse'", "'matmult'", "'matadd'", "'matsub'", "'read_file'", 
                     "'write_file'", "'print'", "'plot'", "'scatter'", "'histogram'", 
                     "'sin'", "'cos'", "'tan'", "'sqrt'", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'^'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "WHILE", "DEF", 
                      "RETURN", "LINEAR_REGRESSION", "MLP_CLASSIFIER", "NEURAL_NETWORK", 
                      "PREDICT", "TRAIN", "TRANSPOSE", "INVERSE", "MATMULT", 
                      "MATADD", "MATSUB", "READ_FILE", "WRITE_FILE", "PRINT", 
                      "PLOT", "SCATTER", "HISTOGRAM", "SIN", "COS", "TAN", 
                      "SQRT", "ASSIGN", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "POWER", "EQ", "NE", "LT", "LE", "GT", "GE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "COMMA", "SEMICOLON", "NUMBER", "FLOAT", 
                      "STRING", "ID", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement_list = 1
    RULE_statement = 2
    RULE_assignment = 3
    RULE_expression = 4
    RULE_expr_rest = 5
    RULE_term = 6
    RULE_term_rest = 7
    RULE_factor = 8
    RULE_factor_rest = 9
    RULE_base = 10
    RULE_unary_expr = 11
    RULE_trig_func = 12
    RULE_matrix_expr = 13
    RULE_matrix_content = 14
    RULE_matrix_content_rest = 15
    RULE_matrix_row = 16
    RULE_expression_list = 17
    RULE_expression_list_rest = 18
    RULE_matrix_operation = 19
    RULE_conditional = 20
    RULE_else_part = 21
    RULE_condition = 22
    RULE_rel_op = 23
    RULE_loop = 24
    RULE_for_loop = 25
    RULE_while_loop = 26
    RULE_function_def = 27
    RULE_param_list = 28
    RULE_param_list_rest = 29
    RULE_return_stmt = 30
    RULE_function_call = 31
    RULE_arg_list = 32
    RULE_arg_list_rest = 33
    RULE_ml_function = 34
    RULE_io_function = 35
    RULE_plot_function = 36

    ruleNames =  [ "program", "statement_list", "statement", "assignment", 
                   "expression", "expr_rest", "term", "term_rest", "factor", 
                   "factor_rest", "base", "unary_expr", "trig_func", "matrix_expr", 
                   "matrix_content", "matrix_content_rest", "matrix_row", 
                   "expression_list", "expression_list_rest", "matrix_operation", 
                   "conditional", "else_part", "condition", "rel_op", "loop", 
                   "for_loop", "while_loop", "function_def", "param_list", 
                   "param_list_rest", "return_stmt", "function_call", "arg_list", 
                   "arg_list_rest", "ml_function", "io_function", "plot_function" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    WHILE=4
    DEF=5
    RETURN=6
    LINEAR_REGRESSION=7
    MLP_CLASSIFIER=8
    NEURAL_NETWORK=9
    PREDICT=10
    TRAIN=11
    TRANSPOSE=12
    INVERSE=13
    MATMULT=14
    MATADD=15
    MATSUB=16
    READ_FILE=17
    WRITE_FILE=18
    PRINT=19
    PLOT=20
    SCATTER=21
    HISTOGRAM=22
    SIN=23
    COS=24
    TAN=25
    SQRT=26
    ASSIGN=27
    PLUS=28
    MINUS=29
    MULT=30
    DIV=31
    MOD=32
    POWER=33
    EQ=34
    NE=35
    LT=36
    LE=37
    GT=38
    GE=39
    LPAREN=40
    RPAREN=41
    LBRACE=42
    RBRACE=43
    LBRACKET=44
    RBRACKET=45
    COMMA=46
    SEMICOLON=47
    NUMBER=48
    FLOAT=49
    STRING=50
    ID=51
    WS=52
    COMMENT=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def EOF(self):
            return self.getToken(DeepLearningDSLParser.EOF, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DeepLearningDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.statement_list()
            self.state = 75
            self.match(DeepLearningDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = DeepLearningDSLParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement_list)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 40, 44, 48, 49, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.statement()
                self.state = 78
                self.statement_list()
                pass
            elif token in [-1, 6, 43]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.AssignmentContext,0)


        def SEMICOLON(self):
            return self.getToken(DeepLearningDSLParser.SEMICOLON, 0)

        def conditional(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ConditionalContext,0)


        def loop(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.LoopContext,0)


        def function_def(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Function_defContext,0)


        def function_call(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Function_callContext,0)


        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DeepLearningDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.assignment()
                self.state = 84
                self.match(DeepLearningDSLParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.conditional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.loop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.function_def()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.function_call()
                self.state = 90
                self.match(DeepLearningDSLParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.expression()
                self.state = 93
                self.match(DeepLearningDSLParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(DeepLearningDSLParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = DeepLearningDSLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(DeepLearningDSLParser.ID)
            self.state = 98
            self.match(DeepLearningDSLParser.ASSIGN)
            self.state = 99
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.TermContext,0)


        def expr_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expr_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = DeepLearningDSLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.term()
            self.state = 102
            self.expr_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(DeepLearningDSLParser.PLUS, 0)

        def term(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.TermContext,0)


        def expr_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expr_restContext,0)


        def MINUS(self):
            return self.getToken(DeepLearningDSLParser.MINUS, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_expr_rest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_rest" ):
                return visitor.visitExpr_rest(self)
            else:
                return visitor.visitChildren(self)




    def expr_rest(self):

        localctx = DeepLearningDSLParser.Expr_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr_rest)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(DeepLearningDSLParser.PLUS)
                self.state = 105
                self.term()
                self.state = 106
                self.expr_rest()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(DeepLearningDSLParser.MINUS)
                self.state = 109
                self.term()
                self.state = 110
                self.expr_rest()
                pass
            elif token in [34, 35, 36, 37, 38, 39, 41, 45, 46, 47]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.FactorContext,0)


        def term_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Term_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = DeepLearningDSLParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.factor()
            self.state = 116
            self.term_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(DeepLearningDSLParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.FactorContext,0)


        def term_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Term_restContext,0)


        def DIV(self):
            return self.getToken(DeepLearningDSLParser.DIV, 0)

        def MOD(self):
            return self.getToken(DeepLearningDSLParser.MOD, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_term_rest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_rest" ):
                return visitor.visitTerm_rest(self)
            else:
                return visitor.visitChildren(self)




    def term_rest(self):

        localctx = DeepLearningDSLParser.Term_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term_rest)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(DeepLearningDSLParser.MULT)
                self.state = 119
                self.factor()
                self.state = 120
                self.term_rest()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(DeepLearningDSLParser.DIV)
                self.state = 123
                self.factor()
                self.state = 124
                self.term_rest()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(DeepLearningDSLParser.MOD)
                self.state = 127
                self.factor()
                self.state = 128
                self.term_rest()
                pass
            elif token in [28, 29, 34, 35, 36, 37, 38, 39, 41, 45, 46, 47]:
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.BaseContext,0)


        def factor_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Factor_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = DeepLearningDSLParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.base()
            self.state = 134
            self.factor_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POWER(self):
            return self.getToken(DeepLearningDSLParser.POWER, 0)

        def base(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.BaseContext,0)


        def factor_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Factor_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_factor_rest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_rest" ):
                return visitor.visitFactor_rest(self)
            else:
                return visitor.visitChildren(self)




    def factor_rest(self):

        localctx = DeepLearningDSLParser.Factor_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor_rest)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(DeepLearningDSLParser.POWER)
                self.state = 137
                self.base()
                self.state = 138
                self.factor_rest()
                pass
            elif token in [28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 41, 45, 46, 47]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def NUMBER(self):
            return self.getToken(DeepLearningDSLParser.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(DeepLearningDSLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(DeepLearningDSLParser.STRING, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def matrix_expr(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Matrix_exprContext,0)


        def function_call(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Function_callContext,0)


        def unary_expr(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Unary_exprContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_base

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase" ):
                return visitor.visitBase(self)
            else:
                return visitor.visitChildren(self)




    def base(self):

        localctx = DeepLearningDSLParser.BaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_base)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(DeepLearningDSLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(DeepLearningDSLParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.match(DeepLearningDSLParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.match(DeepLearningDSLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 148
                self.expression()
                self.state = 149
                self.match(DeepLearningDSLParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
                self.matrix_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 152
                self.function_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 153
                self.unary_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(DeepLearningDSLParser.MINUS, 0)

        def base(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.BaseContext,0)


        def trig_func(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Trig_funcContext,0)


        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_unary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expr" ):
                return visitor.visitUnary_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_expr(self):

        localctx = DeepLearningDSLParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_unary_expr)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(DeepLearningDSLParser.MINUS)
                self.state = 157
                self.base()
                pass
            elif token in [23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.trig_func()
                self.state = 159
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 160
                self.expression()
                self.state = 161
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Trig_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIN(self):
            return self.getToken(DeepLearningDSLParser.SIN, 0)

        def COS(self):
            return self.getToken(DeepLearningDSLParser.COS, 0)

        def TAN(self):
            return self.getToken(DeepLearningDSLParser.TAN, 0)

        def SQRT(self):
            return self.getToken(DeepLearningDSLParser.SQRT, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_trig_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrig_func" ):
                return visitor.visitTrig_func(self)
            else:
                return visitor.visitChildren(self)




    def trig_func(self):

        localctx = DeepLearningDSLParser.Trig_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_trig_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(DeepLearningDSLParser.LBRACKET, 0)

        def matrix_content(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Matrix_contentContext,0)


        def RBRACKET(self):
            return self.getToken(DeepLearningDSLParser.RBRACKET, 0)

        def matrix_operation(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Matrix_operationContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_matrix_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_expr" ):
                return visitor.visitMatrix_expr(self)
            else:
                return visitor.visitChildren(self)




    def matrix_expr(self):

        localctx = DeepLearningDSLParser.Matrix_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_matrix_expr)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(DeepLearningDSLParser.LBRACKET)
                self.state = 168
                self.matrix_content()
                self.state = 169
                self.match(DeepLearningDSLParser.RBRACKET)
                pass
            elif token in [12, 13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.matrix_operation()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrix_row(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Matrix_rowContext,0)


        def matrix_content_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Matrix_content_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_matrix_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_content" ):
                return visitor.visitMatrix_content(self)
            else:
                return visitor.visitChildren(self)




    def matrix_content(self):

        localctx = DeepLearningDSLParser.Matrix_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_matrix_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.matrix_row()
            self.state = 175
            self.matrix_content_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_content_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def matrix_row(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Matrix_rowContext,0)


        def matrix_content_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Matrix_content_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_matrix_content_rest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_content_rest" ):
                return visitor.visitMatrix_content_rest(self)
            else:
                return visitor.visitChildren(self)




    def matrix_content_rest(self):

        localctx = DeepLearningDSLParser.Matrix_content_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_matrix_content_rest)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 178
                self.matrix_row()
                self.state = 179
                self.matrix_content_rest()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_rowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(DeepLearningDSLParser.LBRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expression_listContext,0)


        def RBRACKET(self):
            return self.getToken(DeepLearningDSLParser.RBRACKET, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_matrix_row

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_row" ):
                return visitor.visitMatrix_row(self)
            else:
                return visitor.visitChildren(self)




    def matrix_row(self):

        localctx = DeepLearningDSLParser.Matrix_rowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_matrix_row)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(DeepLearningDSLParser.LBRACKET)
            self.state = 185
            self.expression_list()
            self.state = 186
            self.match(DeepLearningDSLParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def expression_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expression_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = DeepLearningDSLParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.expression()
            self.state = 189
            self.expression_list_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_list_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def expression_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expression_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_expression_list_rest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list_rest" ):
                return visitor.visitExpression_list_rest(self)
            else:
                return visitor.visitChildren(self)




    def expression_list_rest(self):

        localctx = DeepLearningDSLParser.Expression_list_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression_list_rest)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 192
                self.expression()
                self.state = 193
                self.expression_list_rest()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANSPOSE(self):
            return self.getToken(DeepLearningDSLParser.TRANSPOSE, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def INVERSE(self):
            return self.getToken(DeepLearningDSLParser.INVERSE, 0)

        def MATMULT(self):
            return self.getToken(DeepLearningDSLParser.MATMULT, 0)

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def MATADD(self):
            return self.getToken(DeepLearningDSLParser.MATADD, 0)

        def MATSUB(self):
            return self.getToken(DeepLearningDSLParser.MATSUB, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_matrix_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_operation" ):
                return visitor.visitMatrix_operation(self)
            else:
                return visitor.visitChildren(self)




    def matrix_operation(self):

        localctx = DeepLearningDSLParser.Matrix_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_matrix_operation)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(DeepLearningDSLParser.TRANSPOSE)
                self.state = 199
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 200
                self.expression()
                self.state = 201
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(DeepLearningDSLParser.INVERSE)
                self.state = 204
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 205
                self.expression()
                self.state = 206
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.match(DeepLearningDSLParser.MATMULT)
                self.state = 209
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 210
                self.expression()
                self.state = 211
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 212
                self.expression()
                self.state = 213
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.match(DeepLearningDSLParser.MATADD)
                self.state = 216
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 217
                self.expression()
                self.state = 218
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 219
                self.expression()
                self.state = 220
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.match(DeepLearningDSLParser.MATSUB)
                self.state = 223
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 224
                self.expression()
                self.state = 225
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 226
                self.expression()
                self.state = 227
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(DeepLearningDSLParser.IF, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def else_part(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Else_partContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_conditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = DeepLearningDSLParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(DeepLearningDSLParser.IF)
            self.state = 232
            self.match(DeepLearningDSLParser.LPAREN)
            self.state = 233
            self.condition()
            self.state = 234
            self.match(DeepLearningDSLParser.RPAREN)
            self.state = 235
            self.match(DeepLearningDSLParser.LBRACE)
            self.state = 236
            self.statement_list()
            self.state = 237
            self.match(DeepLearningDSLParser.RBRACE)
            self.state = 238
            self.else_part()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(DeepLearningDSLParser.ELSE, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = DeepLearningDSLParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_else_part)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(DeepLearningDSLParser.ELSE)
                self.state = 241
                self.match(DeepLearningDSLParser.LBRACE)
                self.state = 242
                self.statement_list()
                self.state = 243
                self.match(DeepLearningDSLParser.RBRACE)
                pass
            elif token in [-1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 40, 43, 44, 48, 49, 50, 51]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,i)


        def rel_op(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Rel_opContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = DeepLearningDSLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_condition)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.expression()
                self.state = 249
                self.rel_op()
                self.state = 250
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(DeepLearningDSLParser.EQ, 0)

        def NE(self):
            return self.getToken(DeepLearningDSLParser.NE, 0)

        def LT(self):
            return self.getToken(DeepLearningDSLParser.LT, 0)

        def LE(self):
            return self.getToken(DeepLearningDSLParser.LE, 0)

        def GT(self):
            return self.getToken(DeepLearningDSLParser.GT, 0)

        def GE(self):
            return self.getToken(DeepLearningDSLParser.GE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_rel_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = DeepLearningDSLParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_loop(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.For_loopContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.While_loopContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = DeepLearningDSLParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_loop)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.for_loop()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.while_loop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(DeepLearningDSLParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.AssignmentContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLearningDSLParser.SEMICOLON)
            else:
                return self.getToken(DeepLearningDSLParser.SEMICOLON, i)

        def condition(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_for_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = DeepLearningDSLParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(DeepLearningDSLParser.FOR)
            self.state = 262
            self.match(DeepLearningDSLParser.LPAREN)
            self.state = 263
            self.assignment()
            self.state = 264
            self.match(DeepLearningDSLParser.SEMICOLON)
            self.state = 265
            self.condition()
            self.state = 266
            self.match(DeepLearningDSLParser.SEMICOLON)
            self.state = 267
            self.assignment()
            self.state = 268
            self.match(DeepLearningDSLParser.RPAREN)
            self.state = 269
            self.match(DeepLearningDSLParser.LBRACE)
            self.state = 270
            self.statement_list()
            self.state = 271
            self.match(DeepLearningDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(DeepLearningDSLParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_while_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = DeepLearningDSLParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(DeepLearningDSLParser.WHILE)
            self.state = 274
            self.match(DeepLearningDSLParser.LPAREN)
            self.state = 275
            self.condition()
            self.state = 276
            self.match(DeepLearningDSLParser.RPAREN)
            self.state = 277
            self.match(DeepLearningDSLParser.LBRACE)
            self.state = 278
            self.statement_list()
            self.state = 279
            self.match(DeepLearningDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(DeepLearningDSLParser.DEF, 0)

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def param_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Param_listContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Return_stmtContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_function_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = DeepLearningDSLParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_function_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(DeepLearningDSLParser.DEF)
            self.state = 282
            self.match(DeepLearningDSLParser.ID)
            self.state = 283
            self.match(DeepLearningDSLParser.LPAREN)
            self.state = 284
            self.param_list()
            self.state = 285
            self.match(DeepLearningDSLParser.RPAREN)
            self.state = 286
            self.match(DeepLearningDSLParser.LBRACE)
            self.state = 287
            self.statement_list()
            self.state = 288
            self.return_stmt()
            self.state = 289
            self.match(DeepLearningDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def param_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Param_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = DeepLearningDSLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_param_list)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(DeepLearningDSLParser.ID)
                self.state = 292
                self.param_list_rest()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_list_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def param_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Param_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_param_list_rest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list_rest" ):
                return visitor.visitParam_list_rest(self)
            else:
                return visitor.visitChildren(self)




    def param_list_rest(self):

        localctx = DeepLearningDSLParser.Param_list_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_param_list_rest)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 297
                self.match(DeepLearningDSLParser.ID)
                self.state = 298
                self.param_list_rest()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(DeepLearningDSLParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(DeepLearningDSLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = DeepLearningDSLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(DeepLearningDSLParser.RETURN)
            self.state = 303
            self.expression()
            self.state = 304
            self.match(DeepLearningDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def arg_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Arg_listContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def ml_function(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Ml_functionContext,0)


        def io_function(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Io_functionContext,0)


        def plot_function(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Plot_functionContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = DeepLearningDSLParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_function_call)
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(DeepLearningDSLParser.ID)
                self.state = 307
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 308
                self.arg_list()
                self.state = 309
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [7, 8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.ml_function()
                pass
            elif token in [17, 18, 19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.io_function()
                pass
            elif token in [20, 21, 22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.plot_function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def arg_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Arg_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_arg_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = DeepLearningDSLParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_arg_list)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 40, 44, 48, 49, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.expression()
                self.state = 317
                self.arg_list_rest()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_list_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def arg_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Arg_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_arg_list_rest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list_rest" ):
                return visitor.visitArg_list_rest(self)
            else:
                return visitor.visitChildren(self)




    def arg_list_rest(self):

        localctx = DeepLearningDSLParser.Arg_list_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arg_list_rest)
        try:
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 323
                self.expression()
                self.state = 324
                self.arg_list_rest()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ml_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINEAR_REGRESSION(self):
            return self.getToken(DeepLearningDSLParser.LINEAR_REGRESSION, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLearningDSLParser.COMMA)
            else:
                return self.getToken(DeepLearningDSLParser.COMMA, i)

        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def MLP_CLASSIFIER(self):
            return self.getToken(DeepLearningDSLParser.MLP_CLASSIFIER, 0)

        def NEURAL_NETWORK(self):
            return self.getToken(DeepLearningDSLParser.NEURAL_NETWORK, 0)

        def PREDICT(self):
            return self.getToken(DeepLearningDSLParser.PREDICT, 0)

        def TRAIN(self):
            return self.getToken(DeepLearningDSLParser.TRAIN, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_ml_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMl_function" ):
                return visitor.visitMl_function(self)
            else:
                return visitor.visitChildren(self)




    def ml_function(self):

        localctx = DeepLearningDSLParser.Ml_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_ml_function)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(DeepLearningDSLParser.LINEAR_REGRESSION)
                self.state = 330
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 331
                self.expression()
                self.state = 332
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 333
                self.expression()
                self.state = 334
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(DeepLearningDSLParser.MLP_CLASSIFIER)
                self.state = 337
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 338
                self.expression()
                self.state = 339
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 340
                self.expression()
                self.state = 341
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 342
                self.expression()
                self.state = 343
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.match(DeepLearningDSLParser.NEURAL_NETWORK)
                self.state = 346
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 347
                self.expression()
                self.state = 348
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 349
                self.expression()
                self.state = 350
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 351
                self.expression()
                self.state = 352
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.match(DeepLearningDSLParser.PREDICT)
                self.state = 355
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 356
                self.expression()
                self.state = 357
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 358
                self.expression()
                self.state = 359
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 361
                self.match(DeepLearningDSLParser.TRAIN)
                self.state = 362
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 363
                self.expression()
                self.state = 364
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 365
                self.expression()
                self.state = 366
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Io_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ_FILE(self):
            return self.getToken(DeepLearningDSLParser.READ_FILE, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def STRING(self):
            return self.getToken(DeepLearningDSLParser.STRING, 0)

        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def WRITE_FILE(self):
            return self.getToken(DeepLearningDSLParser.WRITE_FILE, 0)

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def PRINT(self):
            return self.getToken(DeepLearningDSLParser.PRINT, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_io_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo_function" ):
                return visitor.visitIo_function(self)
            else:
                return visitor.visitChildren(self)




    def io_function(self):

        localctx = DeepLearningDSLParser.Io_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_io_function)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(DeepLearningDSLParser.READ_FILE)
                self.state = 371
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 372
                self.match(DeepLearningDSLParser.STRING)
                self.state = 373
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(DeepLearningDSLParser.WRITE_FILE)
                self.state = 375
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 376
                self.match(DeepLearningDSLParser.STRING)
                self.state = 377
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 378
                self.expression()
                self.state = 379
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.match(DeepLearningDSLParser.PRINT)
                self.state = 382
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 383
                self.expression()
                self.state = 384
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Plot_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLOT(self):
            return self.getToken(DeepLearningDSLParser.PLOT, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def SCATTER(self):
            return self.getToken(DeepLearningDSLParser.SCATTER, 0)

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def HISTOGRAM(self):
            return self.getToken(DeepLearningDSLParser.HISTOGRAM, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_plot_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlot_function" ):
                return visitor.visitPlot_function(self)
            else:
                return visitor.visitChildren(self)




    def plot_function(self):

        localctx = DeepLearningDSLParser.Plot_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_plot_function)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(DeepLearningDSLParser.PLOT)
                self.state = 389
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 390
                self.expression()
                self.state = 391
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(DeepLearningDSLParser.SCATTER)
                self.state = 394
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 395
                self.expression()
                self.state = 396
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 397
                self.expression()
                self.state = 398
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 400
                self.match(DeepLearningDSLParser.HISTOGRAM)
                self.state = 401
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 402
                self.expression()
                self.state = 403
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





