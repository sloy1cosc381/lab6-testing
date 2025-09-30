from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(inText,inStart,inEnd):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=inText,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=int(inStart), end=int(inEnd), score=0.8)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    print(result)
    return(result)
    # input should be:
    # text: My name is Bond.
    # start: 11
    # end: 15
    # 
    # output should be:
    # text: My name is BIP.
    # items:
    # [
    #     {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    # ]

if __name__ == "__main__": 
    text=input("text: ")
    start=input("start: ")
    end=input("end: ")
    result=sample_run_anonymizer(text,start,end);
