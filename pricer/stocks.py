"""Inner name and public name are needed for frontent- we use this as SSOT"""
stocks = [
    [dict(
        innerName='a',
        publicName='Stock A',
        initial=1,
        sigma=0.2,
        leverage=1),
     dict(
        innerName='etf_a',
        publicName='Leveraged ETF 2XA',
        initial=1,
        sigma=0.2,
        leverage=3
    )
    ],
    [dict(
        innerName='b',
        publicName='Stock B',
        initial=1,
        sigma=0.4,
        leverage=1
    ),

        dict(
        innerName='etf_b',
        publicName='Leveraged ETF 2XB',
        initial=1,
        sigma=0.4,
        leverage=3
    ), ]
]
