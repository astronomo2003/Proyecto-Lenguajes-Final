# Generated from grammar/DeepLearningDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DeepLearningDSLParser import DeepLearningDSLParser
else:
    from DeepLearningDSLParser import DeepLearningDSLParser

# This class defines a complete listener for a parse tree produced by DeepLearningDSLParser.
class DeepLearningDSLListener(ParseTreeListener):

    # Enter a parse tree produced by DeepLearningDSLParser#program.
    def enterProgram(self, ctx:DeepLearningDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#program.
    def exitProgram(self, ctx:DeepLearningDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#statement_list.
    def enterStatement_list(self, ctx:DeepLearningDSLParser.Statement_listContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#statement_list.
    def exitStatement_list(self, ctx:DeepLearningDSLParser.Statement_listContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#statement.
    def enterStatement(self, ctx:DeepLearningDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#statement.
    def exitStatement(self, ctx:DeepLearningDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#assignment.
    def enterAssignment(self, ctx:DeepLearningDSLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#assignment.
    def exitAssignment(self, ctx:DeepLearningDSLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#expression.
    def enterExpression(self, ctx:DeepLearningDSLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#expression.
    def exitExpression(self, ctx:DeepLearningDSLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#expr_rest.
    def enterExpr_rest(self, ctx:DeepLearningDSLParser.Expr_restContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#expr_rest.
    def exitExpr_rest(self, ctx:DeepLearningDSLParser.Expr_restContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#term.
    def enterTerm(self, ctx:DeepLearningDSLParser.TermContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#term.
    def exitTerm(self, ctx:DeepLearningDSLParser.TermContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#term_rest.
    def enterTerm_rest(self, ctx:DeepLearningDSLParser.Term_restContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#term_rest.
    def exitTerm_rest(self, ctx:DeepLearningDSLParser.Term_restContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#factor.
    def enterFactor(self, ctx:DeepLearningDSLParser.FactorContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#factor.
    def exitFactor(self, ctx:DeepLearningDSLParser.FactorContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#factor_rest.
    def enterFactor_rest(self, ctx:DeepLearningDSLParser.Factor_restContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#factor_rest.
    def exitFactor_rest(self, ctx:DeepLearningDSLParser.Factor_restContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#base.
    def enterBase(self, ctx:DeepLearningDSLParser.BaseContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#base.
    def exitBase(self, ctx:DeepLearningDSLParser.BaseContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#unary_expr.
    def enterUnary_expr(self, ctx:DeepLearningDSLParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#unary_expr.
    def exitUnary_expr(self, ctx:DeepLearningDSLParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#trig_func.
    def enterTrig_func(self, ctx:DeepLearningDSLParser.Trig_funcContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#trig_func.
    def exitTrig_func(self, ctx:DeepLearningDSLParser.Trig_funcContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#matrix_expr.
    def enterMatrix_expr(self, ctx:DeepLearningDSLParser.Matrix_exprContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#matrix_expr.
    def exitMatrix_expr(self, ctx:DeepLearningDSLParser.Matrix_exprContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#matrix_content.
    def enterMatrix_content(self, ctx:DeepLearningDSLParser.Matrix_contentContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#matrix_content.
    def exitMatrix_content(self, ctx:DeepLearningDSLParser.Matrix_contentContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#matrix_content_rest.
    def enterMatrix_content_rest(self, ctx:DeepLearningDSLParser.Matrix_content_restContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#matrix_content_rest.
    def exitMatrix_content_rest(self, ctx:DeepLearningDSLParser.Matrix_content_restContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#matrix_row.
    def enterMatrix_row(self, ctx:DeepLearningDSLParser.Matrix_rowContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#matrix_row.
    def exitMatrix_row(self, ctx:DeepLearningDSLParser.Matrix_rowContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#expression_list.
    def enterExpression_list(self, ctx:DeepLearningDSLParser.Expression_listContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#expression_list.
    def exitExpression_list(self, ctx:DeepLearningDSLParser.Expression_listContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#expression_list_rest.
    def enterExpression_list_rest(self, ctx:DeepLearningDSLParser.Expression_list_restContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#expression_list_rest.
    def exitExpression_list_rest(self, ctx:DeepLearningDSLParser.Expression_list_restContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#matrix_operation.
    def enterMatrix_operation(self, ctx:DeepLearningDSLParser.Matrix_operationContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#matrix_operation.
    def exitMatrix_operation(self, ctx:DeepLearningDSLParser.Matrix_operationContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#conditional.
    def enterConditional(self, ctx:DeepLearningDSLParser.ConditionalContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#conditional.
    def exitConditional(self, ctx:DeepLearningDSLParser.ConditionalContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#else_part.
    def enterElse_part(self, ctx:DeepLearningDSLParser.Else_partContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#else_part.
    def exitElse_part(self, ctx:DeepLearningDSLParser.Else_partContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#condition.
    def enterCondition(self, ctx:DeepLearningDSLParser.ConditionContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#condition.
    def exitCondition(self, ctx:DeepLearningDSLParser.ConditionContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#rel_op.
    def enterRel_op(self, ctx:DeepLearningDSLParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#rel_op.
    def exitRel_op(self, ctx:DeepLearningDSLParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#loop.
    def enterLoop(self, ctx:DeepLearningDSLParser.LoopContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#loop.
    def exitLoop(self, ctx:DeepLearningDSLParser.LoopContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#for_loop.
    def enterFor_loop(self, ctx:DeepLearningDSLParser.For_loopContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#for_loop.
    def exitFor_loop(self, ctx:DeepLearningDSLParser.For_loopContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#while_loop.
    def enterWhile_loop(self, ctx:DeepLearningDSLParser.While_loopContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#while_loop.
    def exitWhile_loop(self, ctx:DeepLearningDSLParser.While_loopContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#function_def.
    def enterFunction_def(self, ctx:DeepLearningDSLParser.Function_defContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#function_def.
    def exitFunction_def(self, ctx:DeepLearningDSLParser.Function_defContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#param_list.
    def enterParam_list(self, ctx:DeepLearningDSLParser.Param_listContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#param_list.
    def exitParam_list(self, ctx:DeepLearningDSLParser.Param_listContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#param_list_rest.
    def enterParam_list_rest(self, ctx:DeepLearningDSLParser.Param_list_restContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#param_list_rest.
    def exitParam_list_rest(self, ctx:DeepLearningDSLParser.Param_list_restContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#return_stmt.
    def enterReturn_stmt(self, ctx:DeepLearningDSLParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#return_stmt.
    def exitReturn_stmt(self, ctx:DeepLearningDSLParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#function_call.
    def enterFunction_call(self, ctx:DeepLearningDSLParser.Function_callContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#function_call.
    def exitFunction_call(self, ctx:DeepLearningDSLParser.Function_callContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#arg_list.
    def enterArg_list(self, ctx:DeepLearningDSLParser.Arg_listContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#arg_list.
    def exitArg_list(self, ctx:DeepLearningDSLParser.Arg_listContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#arg_list_rest.
    def enterArg_list_rest(self, ctx:DeepLearningDSLParser.Arg_list_restContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#arg_list_rest.
    def exitArg_list_rest(self, ctx:DeepLearningDSLParser.Arg_list_restContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#ml_function.
    def enterMl_function(self, ctx:DeepLearningDSLParser.Ml_functionContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#ml_function.
    def exitMl_function(self, ctx:DeepLearningDSLParser.Ml_functionContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#io_function.
    def enterIo_function(self, ctx:DeepLearningDSLParser.Io_functionContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#io_function.
    def exitIo_function(self, ctx:DeepLearningDSLParser.Io_functionContext):
        pass


    # Enter a parse tree produced by DeepLearningDSLParser#plot_function.
    def enterPlot_function(self, ctx:DeepLearningDSLParser.Plot_functionContext):
        pass

    # Exit a parse tree produced by DeepLearningDSLParser#plot_function.
    def exitPlot_function(self, ctx:DeepLearningDSLParser.Plot_functionContext):
        pass



del DeepLearningDSLParser