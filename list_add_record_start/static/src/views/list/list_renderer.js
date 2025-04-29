/** @odoo-module **/

import {ListRenderer} from "@web/views/list/list_renderer";
import {patch} from "@web/core/utils/patch";
import {useService} from "@web/core/utils/hooks";
import {session} from "@web/session";

patch(ListRenderer.prototype, {
    setup(){
        super.setup();
        this.orm = useService("orm");
    },

    get addRecordStartLocateButton(){
        return session.add_record_start || false;
    }
})
