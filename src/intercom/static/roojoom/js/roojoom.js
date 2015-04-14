
$(document).ready(function()
{
    createGUI();

    div_frame.addClass('english');
});


function createGUI()
{
    div_control = $('<div>', {

        id: "div_control"
    });

    $("body").append(div_control);

    createControl(div_control);


    div_frame_wrapper = $('<div>', {

        id: "div_frame_wrapper",
        class: "tablewrapper"
    });

    $("body").append(div_frame_wrapper);

    div_frame = $('<div>', {

        id: "div_frame",
        class: "table"
    });

    div_frame_wrapper.append(div_frame);

    createFrame(div_frame);




    div_home_link_wrapper = $('<div>', {

        id: "div_home_link_wrapper",
        class: "row row_wide"
    });

    span_home_link = $('<span>', {

        id: "span_home_link",
        class: "cell cell_wide"
    });

    div_home_link_wrapper.append(span_home_link);

    div_home_link_wrapper.insertAfter(div_middle);

//    div_home_link.insertAfter(div_middle);


    createHomeLink(span_home_link);
};



function createControl(parent_element)
{
    b_english = $('<input>', {

        id: 'b_english',
        class: 'control_buttons',
        val: "English",
        type: "button",
        click: function()
        {
            div_frame.removeClass('hebrew');
            div_frame.removeClass('mobile');
            div_frame.addClass('english');
        }
    });

    parent_element.append(b_english);


    b_hebrew = $('<input>', {

        id: 'b_hebrew',
        class: 'control_buttons',
        val: "Hebrew",
        type:"button",
        click: function()
        {
            div_frame.removeClass('english');
            div_frame.removeClass('mobile');
            div_frame.addClass('hebrew');
        }
    });

    parent_element.append(b_hebrew);

    b_mobile = $('<input>', {

        id: 'b_mobile',
        class: 'control_buttons',
        val: "Mobile",
        type:"button",
        click: function()
        {
            div_frame.removeClass('english');
            div_frame.removeClass('hebrew');
            div_frame.addClass('mobile');
        }
    });

    parent_element.append(b_mobile);
};


function createFrame(parent_element)
{
    div_middle= $('<div>', {

        id: "div_middle",
        class: "row"
    });

    parent_element.append(div_middle);

    createMiddle(div_middle);


    div_pannel = $('<div>', {

        id: "div_pannel",
        class: "row"
    });

    parent_element.append(div_pannel);

    div_ok = $('<div>', {

        id: "div_ok",
        class: "cell"
    });

    div_pannel.append(div_ok);

    createOK(div_ok);

    div_cancel = $('<div>', {

        id: "div_cancel",
        class: "cell"
    });

    div_pannel.append(div_cancel);

    createCancel(div_cancel);
};


function createHomeLink(parent_element)
{
    l_home = $('<a>', {

        id: 'l_home',
        html: "Find out more about us",
        href: "http://www.roojoom.com/"
    });

    parent_element.append(l_home);
};


function createMsg(parent_element)
{
    p_msg = $('<p>', {

        id: 'p_msg',
        html: "Let's get to know you"
    });

    parent_element.append(p_msg);
};



function createMiddle(parent_element)
{
    div_msg= $('<div>', {

        id: "div_msg",
        class: "cell"
    });

    parent_element.append(div_msg);

    createMsg(div_msg);


    div_form = $('<div>', {

        id: "div_form",
        class: "cell"
    });

    parent_element.append(div_form);

    createForm(div_form);
};


function createForm(parent_element)
{
     it_first_name = $('<input>', {

        id: 'it_first_name',
        class: 'form_inputs',
        val: "First Name",
        type:"text"
    });

    parent_element.append(it_first_name);

    parent_element.append('<br>');

    it_last_name = $('<input>', {

        id: 'it_last_name',
        class: 'form_inputs',
        val: "Last Name",
        type:"text"
    });

    parent_element.append(it_last_name);

    parent_element.append('<br>');

    it_phone = $('<input>', {

        id: 'it_phone',
        class: 'form_inputs',
        val: "Phone",
        type:"tel"
    });

    parent_element.append(it_phone);


    parent_element.append('<br>');

    it_email = $('<input>', {

        id: 'it_email',
        class: 'form_inputs',
        val: "Email",
        type:"email"
    });

    parent_element.append(it_email);

    parent_element.append('<br>');

    ta_notes = $('<textarea>', {

        id: 'ta_notes',
        class: 'form_inputs',
        val: "Notes",
        rows: 4,
        cols: 10
    });

    parent_element.append(ta_notes);
}



function createOK(parent_element)
{
    b_ok = $('<input>', {

        id: 'b_ok',
        class: 'op_buttons',
        val: "OK",
        type:"button",
        click: function()
        {
            console.log('OK');
        }
    });

    parent_element.append(b_ok);
};

function createCancel(parent_element)
{
    b_cancel = $('<input>', {

        id: 'b_cancel',
        class: 'op_buttons',
        val: "Cancel",
        type:"button",
        click: function()
        {
            console.log('Cancel');
        }
    });

    parent_element.append(b_cancel);
};
