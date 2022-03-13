# Generated from DSL_grammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DSL_grammarParser import DSL_grammarParser
else:
    from DSL_grammarParser import DSL_grammarParser

# This class defines a complete generic visitor for a parse tree produced by DSL_grammarParser.

class DSL_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DSL_grammarParser#source_code.
    def visitSource_code(self, ctx:DSL_grammarParser.Source_codeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#variables_declaration.
    def visitVariables_declaration(self, ctx:DSL_grammarParser.Variables_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#variable_declaration.
    def visitVariable_declaration(self, ctx:DSL_grammarParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#variable.
    def visitVariable(self, ctx:DSL_grammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#identifier.
    def visitIdentifier(self, ctx:DSL_grammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#letter.
    def visitLetter(self, ctx:DSL_grammarParser.LetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#digit.
    def visitDigit(self, ctx:DSL_grammarParser.DigitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#nenule_digit.
    def visitNenule_digit(self, ctx:DSL_grammarParser.Nenule_digitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#set_of_affirmations.
    def visitSet_of_affirmations(self, ctx:DSL_grammarParser.Set_of_affirmationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#set_of_affirmation.
    def visitSet_of_affirmation(self, ctx:DSL_grammarParser.Set_of_affirmationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#variable_attribution.
    def visitVariable_attribution(self, ctx:DSL_grammarParser.Variable_attributionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#act_description.
    def visitAct_description(self, ctx:DSL_grammarParser.Act_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#story.
    def visitStory(self, ctx:DSL_grammarParser.StoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#stage.
    def visitStage(self, ctx:DSL_grammarParser.StageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#section.
    def visitSection(self, ctx:DSL_grammarParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#flow_description.
    def visitFlow_description(self, ctx:DSL_grammarParser.Flow_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#node.
    def visitNode(self, ctx:DSL_grammarParser.NodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#conditions.
    def visitConditions(self, ctx:DSL_grammarParser.ConditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#operand.
    def visitOperand(self, ctx:DSL_grammarParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#composed_operand.
    def visitComposed_operand(self, ctx:DSL_grammarParser.Composed_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#operation.
    def visitOperation(self, ctx:DSL_grammarParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#function.
    def visitFunction(self, ctx:DSL_grammarParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#condition.
    def visitCondition(self, ctx:DSL_grammarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#string.
    def visitString(self, ctx:DSL_grammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#characters.
    def visitCharacters(self, ctx:DSL_grammarParser.CharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_grammarParser#comments.
    def visitComments(self, ctx:DSL_grammarParser.CommentsContext):
        return self.visitChildren(ctx)



del DSL_grammarParser