# Generated from DSL_grammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DSL_grammarParser import DSL_grammarParser
else:
    from DSL_grammarParser import DSL_grammarParser

# This class defines a complete listener for a parse tree produced by DSL_grammarParser.
class DSL_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by DSL_grammarParser#source_code.
    def enterSource_code(self, ctx:DSL_grammarParser.Source_codeContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#source_code.
    def exitSource_code(self, ctx:DSL_grammarParser.Source_codeContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#variables_declaration.
    def enterVariables_declaration(self, ctx:DSL_grammarParser.Variables_declarationContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#variables_declaration.
    def exitVariables_declaration(self, ctx:DSL_grammarParser.Variables_declarationContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#variable_declaration.
    def enterVariable_declaration(self, ctx:DSL_grammarParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#variable_declaration.
    def exitVariable_declaration(self, ctx:DSL_grammarParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#variable.
    def enterVariable(self, ctx:DSL_grammarParser.VariableContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#variable.
    def exitVariable(self, ctx:DSL_grammarParser.VariableContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#identifier.
    def enterIdentifier(self, ctx:DSL_grammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#identifier.
    def exitIdentifier(self, ctx:DSL_grammarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#letter.
    def enterLetter(self, ctx:DSL_grammarParser.LetterContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#letter.
    def exitLetter(self, ctx:DSL_grammarParser.LetterContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#digit.
    def enterDigit(self, ctx:DSL_grammarParser.DigitContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#digit.
    def exitDigit(self, ctx:DSL_grammarParser.DigitContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#nenule_digit.
    def enterNenule_digit(self, ctx:DSL_grammarParser.Nenule_digitContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#nenule_digit.
    def exitNenule_digit(self, ctx:DSL_grammarParser.Nenule_digitContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#set_of_affirmations.
    def enterSet_of_affirmations(self, ctx:DSL_grammarParser.Set_of_affirmationsContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#set_of_affirmations.
    def exitSet_of_affirmations(self, ctx:DSL_grammarParser.Set_of_affirmationsContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#set_of_affirmation.
    def enterSet_of_affirmation(self, ctx:DSL_grammarParser.Set_of_affirmationContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#set_of_affirmation.
    def exitSet_of_affirmation(self, ctx:DSL_grammarParser.Set_of_affirmationContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#variable_attribution.
    def enterVariable_attribution(self, ctx:DSL_grammarParser.Variable_attributionContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#variable_attribution.
    def exitVariable_attribution(self, ctx:DSL_grammarParser.Variable_attributionContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#act_description.
    def enterAct_description(self, ctx:DSL_grammarParser.Act_descriptionContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#act_description.
    def exitAct_description(self, ctx:DSL_grammarParser.Act_descriptionContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#story.
    def enterStory(self, ctx:DSL_grammarParser.StoryContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#story.
    def exitStory(self, ctx:DSL_grammarParser.StoryContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#stage.
    def enterStage(self, ctx:DSL_grammarParser.StageContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#stage.
    def exitStage(self, ctx:DSL_grammarParser.StageContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#section.
    def enterSection(self, ctx:DSL_grammarParser.SectionContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#section.
    def exitSection(self, ctx:DSL_grammarParser.SectionContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#flow_description.
    def enterFlow_description(self, ctx:DSL_grammarParser.Flow_descriptionContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#flow_description.
    def exitFlow_description(self, ctx:DSL_grammarParser.Flow_descriptionContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#node.
    def enterNode(self, ctx:DSL_grammarParser.NodeContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#node.
    def exitNode(self, ctx:DSL_grammarParser.NodeContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#conditions.
    def enterConditions(self, ctx:DSL_grammarParser.ConditionsContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#conditions.
    def exitConditions(self, ctx:DSL_grammarParser.ConditionsContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#operand.
    def enterOperand(self, ctx:DSL_grammarParser.OperandContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#operand.
    def exitOperand(self, ctx:DSL_grammarParser.OperandContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#composed_operand.
    def enterComposed_operand(self, ctx:DSL_grammarParser.Composed_operandContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#composed_operand.
    def exitComposed_operand(self, ctx:DSL_grammarParser.Composed_operandContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#operation.
    def enterOperation(self, ctx:DSL_grammarParser.OperationContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#operation.
    def exitOperation(self, ctx:DSL_grammarParser.OperationContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#function.
    def enterFunction(self, ctx:DSL_grammarParser.FunctionContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#function.
    def exitFunction(self, ctx:DSL_grammarParser.FunctionContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#condition.
    def enterCondition(self, ctx:DSL_grammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#condition.
    def exitCondition(self, ctx:DSL_grammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#string.
    def enterString(self, ctx:DSL_grammarParser.StringContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#string.
    def exitString(self, ctx:DSL_grammarParser.StringContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#characters.
    def enterCharacters(self, ctx:DSL_grammarParser.CharactersContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#characters.
    def exitCharacters(self, ctx:DSL_grammarParser.CharactersContext):
        pass


    # Enter a parse tree produced by DSL_grammarParser#comments.
    def enterComments(self, ctx:DSL_grammarParser.CommentsContext):
        pass

    # Exit a parse tree produced by DSL_grammarParser#comments.
    def exitComments(self, ctx:DSL_grammarParser.CommentsContext):
        pass



del DSL_grammarParser