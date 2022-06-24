from behave import *

from problems.two_sum import TwoSum

use_step_matcher("re")


@given('I have a list of numbers "(?P<num_list>.+)"')
def step_impl(context, num_list):
    nums = num_list.split(',')
    context.nums = [int(i) for i in nums]



@when('I find two indices whose sum is "(?P<target>.+)"')
def step_impl(context, target):
    twoSum = TwoSum()
    answer = twoSum.twoSumBruteForce(context.nums, int(target))
    context.answer = [int(i) for i in answer]


@then('the answer should be "(?P<answer>.+)"')
def step_impl(context, answer):
    indexes = answer.split(',')
    index_list = [int(i) for i in indexes]
    assert context.answer == index_list, f"Expected: {index_list}, Actual: {context.answer}"