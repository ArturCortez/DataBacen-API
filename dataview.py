import pandas as pd
import helper

df = pd.read_csv("./CSV/csv_file.csv", decimal=",", converters={'valorPago':helper.valToFloat,
                                                            'valorEmpenhado': helper.valToFloat,
                                                            'valorLiquidado': helper.valToFloat,
                                                            'valorRestoCancelado': helper.valToFloat,
                                                            'valorRestoInscrito': helper.valToFloat,
                                                            'valorRestoPago':helper.valToFloat})



print(df[['subfuncao', 'valorEmpenhado', 'valorPago']])


