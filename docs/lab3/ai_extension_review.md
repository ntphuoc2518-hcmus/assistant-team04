\# Lab 3: AI Extension Review



\## Feature

Improve the chatbot fallback response when it does not understand a question.



\## AI-generated changes

The initial implementation added a fallback response that explains a supported topic and provides an example question.



\## Manual review and revisions

1\. Restored the original help-keyword condition so help requests continue to work as intended.

2\. Kept the fallback response focused on supported office-location queries and a concrete example.

3\. Added tests for an unsupported classroom question and a completely unrecognized input.



\## Testing

Ran `py -m pytest -q`. Record the final test result after running the updated tests.



\## Limitations

The chatbot still uses rule-based matching and cannot answer every question. The fallback helps users reformulate questions but does not add new office data or new question-understanding capabilities.

