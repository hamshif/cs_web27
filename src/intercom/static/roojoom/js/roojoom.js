

var mobile = false;

$(document).ready(function()
{
    start_();
});


function start_()
{
    $('body').addClass('google_font');
    createFrame($('body'));

    createWrappedElements();

    layEnglish(div_frame);


    div_control.insertBefore(div_frame);
}


function layEnglish(parent_element)
{
    div_top = $('<div>', {

        id: "div_top",
        class: "table top_english"
    });

    parent_element.append(div_top);


    div_left_top = $('<div>', {

        id: "div_left_top",
        class: "cell"
    });

    div_top.append(div_left_top);


    div_right_top = $('<div>', {

        id: "div_right_top",
        class: "cell"
    });

    div_top.append(div_right_top);

    div_msg.appendTo(div_left_top);

    div_form_fields.appendTo(div_right_top);

    div_rooj.appendTo(div_frame);


    div_bottom = $('<div>', {

        id: "div_bottom",
        class: "table bottom_english"
    });

    div_frame.append(div_bottom);


    div_left_bottom = $('<div>', {

        id: "div_left_bottom",
        class: "cell"
    });

    div_bottom.append(div_left_bottom);


    div_right_bottom = $('<div>', {

        id: "div_right_bottom",
        class: "cell"
    });

    div_bottom.append(div_right_bottom);

    div_ok.appendTo(div_left_bottom);
    div_cancel.appendTo(div_right_bottom);


    div_left_bottom.width(div_left_top.width());


    p_msg.css("margin-top", (div_left_top.height() - p_msg.height() )/2 +"px");
    p_msg.css("margin-left", "5px");

    b_ok.css("margin-top", (div_left_bottom.height() - b_ok.height() )/2 +"px");

    ta_notes.width(div_form_fields.width());
    it_first_name.width(ta_notes.width());
    it_last_name.width(ta_notes.width());
    it_phone.width(ta_notes.width());
    it_email.width(ta_notes.width());

    div_form_fields.height(div_right_top -30);
};



function createFrame(parent_element)
{
    div_frame = $('<div>', {

        id: "div_frame",
        class: "table english"
    });

    parent_element.append(div_frame);
};


function textAreaAdjust(o) {

    console.log('adjusting?');

    o.style.height = "1px";
    o.style.height = (25+o.scrollHeight)+"px";
}


function createWrappedElements()
{

    b_english = $('<input>', {

        id: 'b_english',
        class: 'base',
        val: "English",
        type: "button",
        click: function()
        {
            if(mobile == true)
            {
                mobile = false;

                $('body').empty();
                start_();
            }
            else
            {
                div_frame.removeClass('hebrew');
                div_frame.removeClass('mobile');
                div_frame.addClass('english');

                div_form_fields.appendTo(div_right_top);
                div_msg.appendTo(div_left_top);

                $('body').removeClass('ariel_font');
                $('body').removeClass('mobile_font');
                $('body').addClass('google_font');
            }
        }
    });

    b_hebrew = $('<input>', {

        id: 'b_hebrew',
        class: 'base',
        val: "Hebrew",
        type: "button",
        click: function()
        {
            if(mobile == true)
            {
                mobile = false;

                $('body').empty();


                start_();
            }
            else
            {
                div_frame.removeClass('english');
                div_frame.removeClass('mobile');
                div_frame.addClass('hebrew');


                div_form_fields.appendTo(div_left_top);
                div_msg.appendTo(div_right_top);

                $('body').removeClass('google_font');
                $('body').removeClass('mobile_font');
                $('body').addClass('ariel_font');
            }
        }
    });

    b_mobile = $('<input>', {

        id: 'b_mobile',
        class: 'base',
        val: "Mobile",
        type: "button",
        click: function()
        {
            mobile = true;

            div_frame.removeClass('english');
            div_frame.removeClass('hebrew');
            div_frame.addClass('mobile');


            $('body').removeClass('google_font');
            $('body').removeClass('ariel_font');
            $('body').addClass('mobile_font');


            div_frame.removeClass('table');
            div_left_top.addClass('table');
            div_left_top.removeClass('cell');


            div_left_top.insertAfter(div_top);

            div_left_bottom.removeClass('cell');
            div_left_bottom.addClass('table');
            div_left_bottom.addClass('bottom_english');

            div_left_bottom.css("text-align", "center");

            div_left_bottom.insertAfter(div_bottom);
        }
    });

    div_control = $('<div>', {

        id: "div_control",
        class: "wrapper"
    });

    div_control.append(b_english);
    div_control.append(b_hebrew);
    div_control.append(b_mobile);

    $('body').append(div_control);


    p_msg = $('<p>', {

        id: "p_msg",
        class: "base",
        html: "Let's get to know you"
    });

    div_msg = $('<div>', {

        id: "div_msg",
        class: "wrapper"
    });

    div_msg.append(p_msg);

    $('body').append(div_msg);



    it_first_name = $('<input>', {

        id: 'it_first_name',
        class: 'base form_field',
        val: "First Name",
        type: "text"
    });


    it_last_name = $('<input>', {

        id: 'it_last_name',
        class: 'base form_field',
        val: "Last Name",
        type: "text"
    });


    it_phone = $('<input>', {

        id: 'it_phone',
        class: 'base form_field',
        val: "Phone",
        type: "tel"
    });

    it_email = $('<input>', {

        id: 'it_email',
        class: 'base form_field',
        val: "Last Name",
        type: "email"
    });

    ta_notes = $('<textarea>', {

        id: 'ta_notes',
        class: 'base form_field',
        val: "Notes"
    });


    ta_notes.keyup( function(){textAreaAdjust(this);})



    div_form_fields = $('<div>', {

        id: "div_form_fields",
        class: "wrapper"
    });

    div_form_fields.append(it_first_name);
    div_form_fields.append('<br>');
    div_form_fields.append(it_last_name);
    div_form_fields.append('<br>');
    div_form_fields.append(it_phone);
    div_form_fields.append('<br>');
    div_form_fields.append(it_email);
    div_form_fields.append('<br>');
    div_form_fields.append(ta_notes);

    $('body').append(div_form_fields);


    a_rooj = $('<a>', {

        id: 'a_rooj',
        class: 'base',
        html: "Find out more about us",
        href: "http://www.roojoom.com/"
    });

    div_rooj = $('<div>', {

        id: "div_rooj",
        class: "wrapper"
    });

    div_rooj.append(a_rooj);

    $('body').append(div_rooj);



    b_ok = $('<input>', {

        id: 'b_ok',
        class: 'base  b_big',
        val: "OK",
        type: "button",
        click: function()
        {
            console.log('ok');
        }
    });

    div_ok = $('<div>', {

        id: "div_ok",
        class: "wrapper"
    });

    div_ok.append(b_ok);

    $('body').append(div_ok);



    b_cancel = $('<input>', {

        id: 'b_cancel',
        class: 'base  b_big',
        val: "Cancel",
        type: "button",
        click: function()
        {
            console.log('cancel');
        }
    });

    div_cancel = $('<div>', {

        id: "div_cancel",
        class: "wrapper"
    });

    div_cancel.append(b_cancel);

    $('body').append(div_cancel);


};





