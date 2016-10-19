
def theme(context):
    # gotest theme:
    #   ok   archive/tar    0.011s
    #   FAIL archive/zip    0.022s
    #   ?    compress/gzip  [no test files]
    return context, [
        [ "[0-9]+\.[0-9]+s", "white" ],                      # Test runtimes
        [ "(ok)\s+", "blue", "bold" ],                       # Passing tests
        [ "(\?).*(\[no test files\])", "yellow" ],           # Missing tests
        [ "(FAIL)\s+(.*)\s+", "red,magenta", "bold,normal" ] # Failing tests
    ]
