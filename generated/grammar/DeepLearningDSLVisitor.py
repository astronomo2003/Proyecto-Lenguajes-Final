# Generated from grammar/DeepLearningDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DeepLearningDSLParser import DeepLearningDSLParser
else:
    from DeepLearningDSLParser import DeepLearningDSLParser

# This class defines a complete generic visitor for a parse tree produced by DeepLearningDSLParser.

class DeepLearningDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DeepLearningDSLParser#program.
    def visitProgram(self, ctx:DeepLearningDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#list_expr.
    def visitList_expr(self, ctx:DeepLearningDSLParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#statement_list.
    def visitStatement_list(self, ctx:DeepLearningDSLParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#statement.
    def visitStatement(self, ctx:DeepLearningDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#assignment.
    def visitAssignment(self, ctx:DeepLearningDSLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#expression.
    def visitExpression(self, ctx:DeepLearningDSLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#expr_rest.
    def visitExpr_rest(self, ctx:DeepLearningDSLParser.Expr_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#term.
    def visitTerm(self, ctx:DeepLearningDSLParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#term_rest.
    def visitTerm_rest(self, ctx:DeepLearningDSLParser.Term_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#factor.
    def visitFactor(self, ctx:DeepLearningDSLParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#factor_rest.
    def visitFactor_rest(self, ctx:DeepLearningDSLParser.Factor_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#base.
    def visitBase(self, ctx:DeepLearningDSLParser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#unary_expr.
    def visitUnary_expr(self, ctx:DeepLearningDSLParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#trig_func.
    def visitTrig_func(self, ctx:DeepLearningDSLParser.Trig_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#matrix_expr.
    def visitMatrix_expr(self, ctx:DeepLearningDSLParser.Matrix_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#matrix_content.
    def visitMatrix_content(self, ctx:DeepLearningDSLParser.Matrix_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#matrix_content_rest.
    def visitMatrix_content_rest(self, ctx:DeepLearningDSLParser.Matrix_content_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#matrix_row.
    def visitMatrix_row(self, ctx:DeepLearningDSLParser.Matrix_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#expression_list.
    def visitExpression_list(self, ctx:DeepLearningDSLParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#expression_list_rest.
    def visitExpression_list_rest(self, ctx:DeepLearningDSLParser.Expression_list_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#matrix_operation.
    def visitMatrix_operation(self, ctx:DeepLearningDSLParser.Matrix_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#conditional.
    def visitConditional(self, ctx:DeepLearningDSLParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#else_part.
    def visitElse_part(self, ctx:DeepLearningDSLParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#condition.
    def visitCondition(self, ctx:DeepLearningDSLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#rel_op.
    def visitRel_op(self, ctx:DeepLearningDSLParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#loop.
    def visitLoop(self, ctx:DeepLearningDSLParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#for_loop.
    def visitFor_loop(self, ctx:DeepLearningDSLParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#while_loop.
    def visitWhile_loop(self, ctx:DeepLearningDSLParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#function_def.
    def visitFunction_def(self, ctx:DeepLearningDSLParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#param_list.
    def visitParam_list(self, ctx:DeepLearningDSLParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#param_list_rest.
    def visitParam_list_rest(self, ctx:DeepLearningDSLParser.Param_list_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#return_stmt.
    def visitReturn_stmt(self, ctx:DeepLearningDSLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#function_call.
    def visitFunction_call(self, ctx:DeepLearningDSLParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#arg_list.
    def visitArg_list(self, ctx:DeepLearningDSLParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#arg_list_rest.
    def visitArg_list_rest(self, ctx:DeepLearningDSLParser.Arg_list_restContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#ml_function.
    def visitMl_function(self, ctx:DeepLearningDSLParser.Ml_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#io_function.
    def visitIo_function(self, ctx:DeepLearningDSLParser.Io_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepLearningDSLParser#plot_function.
    def visitPlot_function(self, ctx:DeepLearningDSLParser.Plot_functionContext):
        return self.visitChildren(ctx)



del DeepLearningDSLParser