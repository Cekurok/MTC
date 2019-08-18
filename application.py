def dom_shadow(driver, s="1231"):
    search_field = driver.execute_script('return document.querySelector("mts-text-field").shadowRoot.querySelector("input")')
    search_field.click()
    search_field.send_keys("%s" % s)

