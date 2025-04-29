/** @odoo-module */
import {useService} from '@web/core/utils/hooks';
import {Component,onWillStart, useState} from "@odoo/owl";
import { session } from "@web/session";

export class SaleDashBoard extends Component {
    static template = "owl_sale_dashboard.SaleDashboard";
    static props = {};

    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.state = useState({ saleData: null, show: session.view_dashboard });

        onWillStart(async () => {
            if (this.state.show){
                const data = await this.orm.call("sale.order", "retrieve_dashboard");
                this.state.saleData = data;
            }
        });
    }
}